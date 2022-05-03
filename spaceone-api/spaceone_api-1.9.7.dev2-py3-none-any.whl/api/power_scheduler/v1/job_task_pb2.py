# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/power_scheduler/v1/job_task.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v1 import query_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_query__pb2
from spaceone.api.power_scheduler.v1 import job_pb2 as spaceone_dot_api_dot_power__scheduler_dot_v1_dot_job__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.spaceone/api/power_scheduler/v1/job_task.proto\x12\x1fspaceone.api.power_scheduler.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\x1a)spaceone/api/power_scheduler/v1/job.proto\"\x92\x04\n\x0cJobTaskQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x13\n\x0bjob_task_id\x18\x02 \x01(\t\x12K\n\x06status\x18\x03 \x01(\x0e\x32;.spaceone.api.power_scheduler.v1.JobTaskQuery.JobTaskStatus\x12\x0e\n\x06job_id\x18\x04 \x01(\t\x12S\n\x0e\x63ontrol_action\x18\x05 \x01(\x0e\x32;.spaceone.api.power_scheduler.v1.JobTaskQuery.ControlAction\x12\x13\n\x0bschedule_id\x18\x06 \x01(\t\x12\x19\n\x11resource_group_id\x18\x07 \x01(\t\x12\x12\n\nproject_id\x18\x08 \x01(\t\x12\x11\n\tdomain_id\x18\t \x01(\t\"|\n\rJobTaskStatus\x12\x18\n\x14JOB_TASK_STATUS_NONE\x10\x00\x12\x0b\n\x07\x43REATED\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\x0c\n\x08\x43\x41NCELED\x10\x03\x12\x0f\n\x0bIN_PROGRESS\x10\x04\x12\x0b\n\x07SUCCESS\x10\x05\x12\x0b\n\x07\x46\x41ILURE\x10\x06\":\n\rControlAction\x12\x0f\n\x0b\x41\x43TION_NONE\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\x0b\n\x07STOPPED\x10\x02\"\xa9\x05\n\x0bJobTaskInfo\x12\x13\n\x0bjob_task_id\x18\x01 \x01(\t\x12J\n\x06status\x18\x02 \x01(\x0e\x32:.spaceone.api.power_scheduler.v1.JobTaskInfo.JobTaskStatus\x12\x15\n\rsuccess_count\x18\x04 \x01(\x05\x12\x15\n\rfailure_count\x18\x05 \x01(\x05\x12\x13\n\x0btotal_count\x18\x06 \x01(\x05\x12:\n\x06\x65rrors\x18\x07 \x03(\x0b\x32*.spaceone.api.power_scheduler.v1.ErrorInfo\x12\x0e\n\x06job_id\x18\x08 \x01(\t\x12R\n\x0e\x63ontrol_action\x18\t \x01(\x0e\x32:.spaceone.api.power_scheduler.v1.JobTaskInfo.ControlAction\x12\x13\n\x0bschedule_id\x18\n \x01(\t\x12\x19\n\x11resource_group_id\x18\x0b \x01(\t\x12\x10\n\x08priority\x18\x0c \x01(\x05\x12\x12\n\nproject_id\x18\r \x01(\t\x12\x11\n\tdomain_id\x18\x0e \x01(\t\x12\x12\n\ncreated_at\x18\x15 \x01(\t\x12\x12\n\nstarted_at\x18\x16 \x01(\t\x12\x13\n\x0b\x66inished_at\x18\x17 \x01(\t\"l\n\rJobTaskStatus\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07\x43REATED\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\x0c\n\x08\x43\x41NCELED\x10\x03\x12\x0f\n\x0bIN_PROGRESS\x10\x04\x12\x0b\n\x07SUCCESS\x10\x05\x12\x0b\n\x07\x46\x41ILURE\x10\x06\"B\n\rControlAction\x12\x17\n\x13\x43ONTROL_ACTION_NONE\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\x0b\n\x07STOPPED\x10\x02\"b\n\x0cJobTasksInfo\x12=\n\x07results\x18\x01 \x03(\x0b\x32,.spaceone.api.power_scheduler.v1.JobTaskInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"[\n\x10JobTaskStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t2\xbf\x02\n\x07JobTask\x12\xb3\x01\n\x04list\x12-.spaceone.api.power_scheduler.v1.JobTaskQuery\x1a-.spaceone.api.power_scheduler.v1.JobTasksInfo\"M\x82\xd3\xe4\x93\x02G\x12\x1d/power-scheduler/v1/job-tasksZ&\"$/power-scheduler/v1/job-tasks/search\x12~\n\x04stat\x12\x31.spaceone.api.power_scheduler.v1.JobTaskStatQuery\x1a\x17.google.protobuf.Struct\"*\x82\xd3\xe4\x93\x02$\"\"/power-scheduler/v1/job-tasks/statb\x06proto3')



_JOBTASKQUERY = DESCRIPTOR.message_types_by_name['JobTaskQuery']
_JOBTASKINFO = DESCRIPTOR.message_types_by_name['JobTaskInfo']
_JOBTASKSINFO = DESCRIPTOR.message_types_by_name['JobTasksInfo']
_JOBTASKSTATQUERY = DESCRIPTOR.message_types_by_name['JobTaskStatQuery']
_JOBTASKQUERY_JOBTASKSTATUS = _JOBTASKQUERY.enum_types_by_name['JobTaskStatus']
_JOBTASKQUERY_CONTROLACTION = _JOBTASKQUERY.enum_types_by_name['ControlAction']
_JOBTASKINFO_JOBTASKSTATUS = _JOBTASKINFO.enum_types_by_name['JobTaskStatus']
_JOBTASKINFO_CONTROLACTION = _JOBTASKINFO.enum_types_by_name['ControlAction']
JobTaskQuery = _reflection.GeneratedProtocolMessageType('JobTaskQuery', (_message.Message,), {
  'DESCRIPTOR' : _JOBTASKQUERY,
  '__module__' : 'spaceone.api.power_scheduler.v1.job_task_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.power_scheduler.v1.JobTaskQuery)
  })
_sym_db.RegisterMessage(JobTaskQuery)

JobTaskInfo = _reflection.GeneratedProtocolMessageType('JobTaskInfo', (_message.Message,), {
  'DESCRIPTOR' : _JOBTASKINFO,
  '__module__' : 'spaceone.api.power_scheduler.v1.job_task_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.power_scheduler.v1.JobTaskInfo)
  })
_sym_db.RegisterMessage(JobTaskInfo)

JobTasksInfo = _reflection.GeneratedProtocolMessageType('JobTasksInfo', (_message.Message,), {
  'DESCRIPTOR' : _JOBTASKSINFO,
  '__module__' : 'spaceone.api.power_scheduler.v1.job_task_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.power_scheduler.v1.JobTasksInfo)
  })
_sym_db.RegisterMessage(JobTasksInfo)

JobTaskStatQuery = _reflection.GeneratedProtocolMessageType('JobTaskStatQuery', (_message.Message,), {
  'DESCRIPTOR' : _JOBTASKSTATQUERY,
  '__module__' : 'spaceone.api.power_scheduler.v1.job_task_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.power_scheduler.v1.JobTaskStatQuery)
  })
_sym_db.RegisterMessage(JobTaskStatQuery)

_JOBTASK = DESCRIPTOR.services_by_name['JobTask']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _JOBTASK.methods_by_name['list']._options = None
  _JOBTASK.methods_by_name['list']._serialized_options = b'\202\323\344\223\002G\022\035/power-scheduler/v1/job-tasksZ&\"$/power-scheduler/v1/job-tasks/search'
  _JOBTASK.methods_by_name['stat']._options = None
  _JOBTASK.methods_by_name['stat']._serialized_options = b'\202\323\344\223\002$\"\"/power-scheduler/v1/job-tasks/stat'
  _JOBTASKQUERY._serialized_start=221
  _JOBTASKQUERY._serialized_end=751
  _JOBTASKQUERY_JOBTASKSTATUS._serialized_start=567
  _JOBTASKQUERY_JOBTASKSTATUS._serialized_end=691
  _JOBTASKQUERY_CONTROLACTION._serialized_start=693
  _JOBTASKQUERY_CONTROLACTION._serialized_end=751
  _JOBTASKINFO._serialized_start=754
  _JOBTASKINFO._serialized_end=1435
  _JOBTASKINFO_JOBTASKSTATUS._serialized_start=1259
  _JOBTASKINFO_JOBTASKSTATUS._serialized_end=1367
  _JOBTASKINFO_CONTROLACTION._serialized_start=1369
  _JOBTASKINFO_CONTROLACTION._serialized_end=1435
  _JOBTASKSINFO._serialized_start=1437
  _JOBTASKSINFO._serialized_end=1535
  _JOBTASKSTATQUERY._serialized_start=1537
  _JOBTASKSTATQUERY._serialized_end=1628
  _JOBTASK._serialized_start=1631
  _JOBTASK._serialized_end=1950
# @@protoc_insertion_point(module_scope)
