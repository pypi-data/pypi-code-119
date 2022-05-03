from typing import Any, Generic, Optional, Union

from pyntone.models.field import UpdateKey
from pyntone.models.record import DeleteRecord, UpdateRecord
from pyntone.simple.client.types import (AddRecordResponse, AddRecordsResponse,
                                         DeleteRecordsResponse, ResponseRecord,
                                         ResponseRecords, UpdateRecordResponse,
                                         UpdateRecordsResponse, Record)
from pyntone.simple.http.http_client import HttpClent
from pyntone.simple.kintone_request_config_builder import KintoneRequestParams
from pyntone.url import build_path


class RecordClient:
    def __init__(self, http_client: HttpClent, guest_space_id: Union[None, int, str] = None):
        self.http_client = http_client
        self.guest_space_id = guest_space_id

    def get_record(self, app_id: Union[int, str], id: Union[int, str]) -> ResponseRecord:
        params = KintoneRequestParams(url_params={'app': app_id, 'id': id})
        path = self._build_path_with_guest_space_id('record')
        data = self.http_client.get(path, params)
        return ResponseRecord(record=Record(data['record']))

    def get_records(self, app_id: Union[int, str], fields: Optional[list[str]] = None, query: Optional[str] = None, total_count: bool = True) -> ResponseRecords:
        params = KintoneRequestParams(
            url_params={
                'app': app_id,
                'fields': fields,
                'query': query,
                'totalCount': total_count
            }
        )
        path = self._build_path_with_guest_space_id('records')
        data = self.http_client.get(path, params)
        records = [ Record(i) for i in data['records'] ]
        return ResponseRecords(records=records, total_count=int(data['totalCount']))

    def add_record(self, record: dict[str, Any], app_id: Union[int, str, None]=None) -> AddRecordResponse:
        params = KintoneRequestParams(
            data = {
                'app': self._get_app_id(app_id),
                'record': self._convert_data(record)
            }
        )
        path = self._build_path_with_guest_space_id('record')
        data = self.http_client.post(path, params)
        return AddRecordResponse(**data)
    
    def add_records(self, records: list[dict[str, Any]], app_id: Union[int, str, None]=None) -> AddRecordsResponse:
        params = KintoneRequestParams(
            data = {
                'app': self._get_app_id(app_id),
                'records': [ self._convert_data(record) for record in records ]
            }
        )
        path = self._build_path_with_guest_space_id('records')
        data = self.http_client.post(path, params)
        return AddRecordsResponse(**data)

    def update_record(self, key: Union[int, str, UpdateKey], record: dict[str, Any], revision: Union[int, str, None] = None, app_id: Union[int, str, None]=None) -> UpdateRecordResponse:        
        params = KintoneRequestParams(data=UpdateRecord(key=key, record=record, revision=revision).data())
        path = self._build_path_with_guest_space_id('record')
        data = self.http_client.put(path, params)
        return UpdateRecordResponse(**data)
    
    def update_records(self, update_records: list[UpdateRecord], app_id: Union[int, str, None]=None) -> UpdateRecordsResponse:
        params = KintoneRequestParams(
            data = {
                'app': self._get_app_id(app_id),
                'records': [ record.data() for record in update_records ]
            }
        )
        path = self._build_path_with_guest_space_id('records')
        data = self.http_client.put(path, params)
        return UpdateRecordsResponse(**data)
    
    def delete_records(self, ids: list[Union[int, str, DeleteRecord]], app_id: Union[int, str, None]=None) -> DeleteRecordsResponse:
        has_delete_record = False
        data = {
            'app': self._get_app_id(app_id),
            'ids': [],
        }
        revisions = []
        for i in ids:
            if type(i) is DeleteRecord:
                data['ids'].append(i.id)
                revisions.append(i.revision)
                has_delete_record = True
            else:
                data['ids'].append(i)
                revisions.append(-1)
        
        if has_delete_record:
            data['revisions'] = revisions
        
        params = KintoneRequestParams(data=data)
        path = self._build_path_with_guest_space_id('records')
        data = self.http_client.delete(path, params)
        return DeleteRecordsResponse(value=data)
    
    def _convert_data(self, data: dict) -> dict:
        return { key: { 'value': val } for key, val in data.items() }
    
    def _get_app_id(self, app_id: Union[int, str, None]) -> Union[int, str]:
        if app_id is None:
            if self.default_app_id is None:
                raise ValueError('App ID is None')
            else:
                return self.default_app_id
        else:
            return app_id
    
    def _build_path_with_guest_space_id(self, endpoint_name: str) -> str:
        return build_path(endpoint=endpoint_name, guest_space_id=self.guest_space_id)
