from sCoda import Sequence, Composition
from sCoda.elements.message import MessageType
from sCoda.settings import PPQN
from sCoda.util.midi_wrapper import MidiFile
from sCoda.util.util import digitise_velocity, bin_from_velocity


# General

def test_midi_to_sequences():
    midi_file = MidiFile.open_midi_file("resources/beethoven_o27-2_m3.mid")
    sequences = midi_file.to_sequences([[1], [2]], [0, 3])

    assert len(sequences) == 2

    return sequences


def test_split_into_bars():
    sequences = test_midi_to_sequences()
    bars = Sequence.split_into_bars(sequences)

    assert len(bars) == 2
    assert len(bars[0]) == len(bars[1])

    return bars


def test_load_composition():
    composition = Composition.from_file("resources/beethoven_o27-2_m3.mid", [[1], [2]], [0, 3])

    assert len(composition.tracks) == 2

    return composition


# Relative Sequence

def test_adjust_wait_messages():
    sequences = test_midi_to_sequences()
    sequence = sequences[0]
    sequence.adjust_wait_messages()

    assert all((not (msg.message_type == MessageType.wait) or msg.time <= PPQN) for msg in sequence._get_rel().messages)


def test_consolidate_sequences():
    sequences = test_midi_to_sequences()
    sequence = Sequence()
    sequence.consolidate(sequences[0])
    sequence.consolidate(sequences[1])

    assert all(msg in sequence._get_rel().messages for msg in sequences[0]._get_rel().messages)
    assert all(msg in sequence._get_rel().messages for msg in sequences[1]._get_rel().messages)


def test_difficulty_assessment():
    bars = test_split_into_bars()
    bar = bars[0][0]
    difficulty = bar.difficulty

    assert 0 <= difficulty <= 1


def test_pad_sequence():
    sequences = test_midi_to_sequences()
    sequence = sequences[0]

    assert sum(
        msg.time for msg in sequence._get_rel().messages if msg.message_type == MessageType.wait) < PPQN * 4 * 300

    sequence.pad_sequence(PPQN * 4 * 300)

    assert sum(
        msg.time for msg in sequence._get_rel().messages if msg.message_type == MessageType.wait) >= PPQN * 4 * 300


def test_split():
    sequences = test_midi_to_sequences()
    sequence = sequences[0]

    split_up = sequence.split([4 * PPQN])

    assert sum(
        msg.time for msg in split_up[0]._get_rel().messages if msg.message_type == MessageType.wait) == 4 * PPQN


def test_transpose():
    sequences = test_midi_to_sequences()
    sequence = sequences[0]

    note_heights = [msg.note for msg in sequence._get_rel().messages if
                    msg.message_type == MessageType.note_on or msg.message_type == MessageType.note_off]

    had_to_wrap = sequence.transpose(1)

    assert not had_to_wrap

    note_heights_after_quantization = [msg.note for msg in sequence._get_rel().messages if
                                       msg.message_type == MessageType.note_on
                                       or msg.message_type == MessageType.note_off]

    assert all(
        note_heights_after_quantization[i] == note_heights[i] + 1 for i in range(len(note_heights_after_quantization)))


# Absolute Sequence

def test_get_timing_of_message_type():
    sequences = test_midi_to_sequences()
    sequence = sequences[0]

    timings = sequence.get_timing_of_message_type(MessageType.time_signature)
    points_in_time = [timing[0] - timings[i - 1][0] if i >= 1 else timing[0] for i, timing in enumerate(timings)]

    split_sequences = sequence.split(points_in_time)

    assert all(len(seq.get_timing_of_message_type(MessageType.time_signature)) <= 1 for seq in split_sequences)


def test_merge_sequences():
    sequences = test_midi_to_sequences()
    sequence = Sequence()

    sequence.merge(sequences)

    assert len(sequence._get_abs().messages) == len(sequences[0]._get_abs().messages) + len(
        sequences[1]._get_abs().messages)


def test_quantise():
    sequences = test_midi_to_sequences()
    sequence = sequences[0]

    sequence.quantise([PPQN])

    assert all(msg.time % PPQN == 0 for msg in sequence._get_abs().messages)


def test_quantise_note_lengths():
    sequences = test_midi_to_sequences()
    sequence = sequences[0]

    sequence.quantise([PPQN])
    sequence.quantise_note_lengths()


# Util

def test_velocity_values_digitised_to_correct_bins():
    values_to_digitise = [(1, 16), (17, 16), (31, 32), (33, 32), (126, 127)]

    for pair in values_to_digitise:
        assert digitise_velocity(pair[0]) == pair[1]


def test_velocity_digitised_to_correct_bin_indices():
    values_to_digitise = [(1, 0), (17, 0), (31, 1), (33, 1)]

    for pair in values_to_digitise:
        assert bin_from_velocity(pair[0]) == pair[1]
