import os
import signal
import sys

from metadrive.envs.real_data_envs.waymo_env import WaymoEnv
from metadrive.policy.idm_policy import WaymoIDMPolicy
from tqdm import tqdm

try:
    from metadrive.utils.waymo_utils.waymo_utils import AgentType
    from metadrive.utils.waymo_utils.waymo_utils import RoadEdgeType
    from metadrive.utils.waymo_utils.waymo_utils import RoadLineType
finally:
    pass


def handler(signum, frame):
    raise Exception("end of time")


if __name__ == "__main__":
    case_data_path = sys.argv[1]
    processed_data_path = case_data_path + "_filtered"
    if not os.path.exists(processed_data_path):
        os.mkdir(processed_data_path)
    if not os.path.exists(case_data_path) or not os.path.exists(processed_data_path):
        raise ValueError("Path Not exist")
    case_num = len(os.listdir(case_data_path))
    max_step = 1000
    min_step = 100

    env = WaymoEnv(
        {
            "use_render": False,
            "agent_policy": WaymoIDMPolicy,
            "waymo_data_directory": case_data_path,
            "case_num": case_num,
            "store_map": False,
            # "manual_control": True,
            # "debug":True,
            "horizon": 1000,
        }
    )
    try:
        env.reset()
    except:
        pass
    finally:
        pass
    for i in tqdm(range(case_num)):
        try:
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(10)
            env.reset(force_seed=i)
            while True:
                o, r, d, info = env.step([0, 0])
                if d or env.episode_steps > max_step:
                    if info["arrive_dest"] and env.episode_steps > min_step:
                        os.rename(
                            os.path.join(case_data_path, "{}.pkl".format(i)),
                            os.path.join(processed_data_path, "{}.pkl".format(i))
                        )
                    break
        except:
            # print("\n No Route or Timeout, Fail, Seed: {}".format(i))
            pass
