"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1 (v1)
    Contact: support@bimdata.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import bimdata_api_client
from bimdata_api_client.api.collaboration_api import CollaborationApi  # noqa: E501


class TestCollaborationApi(unittest.TestCase):
    """CollaborationApi unit test stubs"""

    def setUp(self):
        self.api = CollaborationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accept_validation(self):
        """Test case for accept_validation

        Accept a validation  # noqa: E501
        """
        pass

    def test_add_document_tag(self):
        """Test case for add_document_tag

        Add a tag to a document  # noqa: E501
        """
        pass

    def test_add_group_member(self):
        """Test case for add_group_member

        Add a user to a group  # noqa: E501
        """
        pass

    def test_cancel_cloud_user_invitation(self):
        """Test case for cancel_cloud_user_invitation

        Cancel a pending invitation  # noqa: E501
        """
        pass

    def test_cancel_project_user_invitation(self):
        """Test case for cancel_project_user_invitation

        Cancel a pending invitation  # noqa: E501
        """
        pass

    def test_check_access(self):
        """Test case for check_access

        Check app access from cloud  # noqa: E501
        """
        pass

    def test_close_visa(self):
        """Test case for close_visa

        Close a visa of a document  # noqa: E501
        """
        pass

    def test_create_classification(self):
        """Test case for create_classification

        Create a classification  # noqa: E501
        """
        pass

    def test_create_cloud(self):
        """Test case for create_cloud

        Create a cloud  # noqa: E501
        """
        pass

    def test_create_demo(self):
        """Test case for create_demo

        Create a Demo project in a cloud  # noqa: E501
        """
        pass

    def test_create_dms_tree(self):
        """Test case for create_dms_tree

        Create a complete DMS tree  # noqa: E501
        """
        pass

    def test_create_document(self):
        """Test case for create_document

        Create a document  # noqa: E501
        """
        pass

    def test_create_folder(self):
        """Test case for create_folder

        Create a folder  # noqa: E501
        """
        pass

    def test_create_manage_group(self):
        """Test case for create_manage_group

        Create a group  # noqa: E501
        """
        pass

    def test_create_project(self):
        """Test case for create_project

        Create a project  # noqa: E501
        """
        pass

    def test_create_project_access_token(self):
        """Test case for create_project_access_token

        Create a token for this project  # noqa: E501
        """
        pass

    def test_create_tag(self):
        """Test case for create_tag

        Create a tag  # noqa: E501
        """
        pass

    def test_create_validation(self):
        """Test case for create_validation

        Add a validation to a visa  # noqa: E501
        """
        pass

    def test_create_visa(self):
        """Test case for create_visa

        Create a visa  # noqa: E501
        """
        pass

    def test_create_visa_comment(self):
        """Test case for create_visa_comment

        Add a comment  # noqa: E501
        """
        pass

    def test_delete_classification(self):
        """Test case for delete_classification

        Delete a classification  # noqa: E501
        """
        pass

    def test_delete_cloud(self):
        """Test case for delete_cloud

        Delete a cloud  # noqa: E501
        """
        pass

    def test_delete_cloud_user(self):
        """Test case for delete_cloud_user

        Remove a user from a cloud  # noqa: E501
        """
        pass

    def test_delete_document(self):
        """Test case for delete_document

        Delete the document  # noqa: E501
        """
        pass

    def test_delete_document_history(self):
        """Test case for delete_document_history

        Delete the document  # noqa: E501
        """
        pass

    def test_delete_document_tag(self):
        """Test case for delete_document_tag

        Delete a tag from a document  # noqa: E501
        """
        pass

    def test_delete_folder(self):
        """Test case for delete_folder

        Delete a folder  # noqa: E501
        """
        pass

    def test_delete_group_member(self):
        """Test case for delete_group_member

        Delete a user from a group  # noqa: E501
        """
        pass

    def test_delete_manage_group(self):
        """Test case for delete_manage_group

        Delete a group  # noqa: E501
        """
        pass

    def test_delete_project(self):
        """Test case for delete_project

        Delete a project  # noqa: E501
        """
        pass

    def test_delete_project_access_token(self):
        """Test case for delete_project_access_token

        Delete a token  # noqa: E501
        """
        pass

    def test_delete_project_user(self):
        """Test case for delete_project_user

        Remove a user from a project  # noqa: E501
        """
        pass

    def test_delete_tag(self):
        """Test case for delete_tag

        Delete the tag  # noqa: E501
        """
        pass

    def test_delete_validation(self):
        """Test case for delete_validation

        Remove a validation  # noqa: E501
        """
        pass

    def test_delete_visa(self):
        """Test case for delete_visa

        Remove a visa  # noqa: E501
        """
        pass

    def test_delete_visa_comment(self):
        """Test case for delete_visa_comment

        Remove a comment  # noqa: E501
        """
        pass

    def test_deny_validation(self):
        """Test case for deny_validation

        Deny a validation  # noqa: E501
        """
        pass

    def test_exit_version_document_history(self):
        """Test case for exit_version_document_history

        Exit of the history version  # noqa: E501
        """
        pass

    def test_get_classification(self):
        """Test case for get_classification

        Retrieve a classification  # noqa: E501
        """
        pass

    def test_get_classifications(self):
        """Test case for get_classifications

        Retrieve all classifications  # noqa: E501
        """
        pass

    def test_get_cloud(self):
        """Test case for get_cloud

        Retrieve one cloud  # noqa: E501
        """
        pass

    def test_get_cloud_invitations(self):
        """Test case for get_cloud_invitations

        Retrieve all pending invitations in the cloud  # noqa: E501
        """
        pass

    def test_get_cloud_size(self):
        """Test case for get_cloud_size

        Get size of the cloud  # noqa: E501
        """
        pass

    def test_get_cloud_user(self):
        """Test case for get_cloud_user

        Retrieve a user in a cloud  # noqa: E501
        """
        pass

    def test_get_cloud_users(self):
        """Test case for get_cloud_users

        Retrieve all users in a cloud, or a list with a filter by email  # noqa: E501
        """
        pass

    def test_get_clouds(self):
        """Test case for get_clouds

        Retrieve all clouds  # noqa: E501
        """
        pass

    def test_get_document(self):
        """Test case for get_document

        Retrieve a document  # noqa: E501
        """
        pass

    def test_get_document_histories(self):
        """Test case for get_document_histories

        Retrieve all document histories  # noqa: E501
        """
        pass

    def test_get_document_history(self):
        """Test case for get_document_history

        Retrieve a document  # noqa: E501
        """
        pass

    def test_get_documents(self):
        """Test case for get_documents

        Retrieve all documents  # noqa: E501
        """
        pass

    def test_get_folder(self):
        """Test case for get_folder

        Retrieve a folder  # noqa: E501
        """
        pass

    def test_get_folder_project_users(self):
        """Test case for get_folder_project_users

        Retrieve all users in a project with the permission on the folder  # noqa: E501
        """
        pass

    def test_get_folders(self):
        """Test case for get_folders

        Retrieve all folders  # noqa: E501
        """
        pass

    def test_get_group(self):
        """Test case for get_group

        Retrieve a group  # noqa: E501
        """
        pass

    def test_get_groups(self):
        """Test case for get_groups

        Retrieve all groups  # noqa: E501
        """
        pass

    def test_get_manage_group(self):
        """Test case for get_manage_group

        Retrieve a group  # noqa: E501
        """
        pass

    def test_get_manage_groups(self):
        """Test case for get_manage_groups

        Retrieve all groups  # noqa: E501
        """
        pass

    def test_get_project(self):
        """Test case for get_project

        Retrieve a project  # noqa: E501
        """
        pass

    def test_get_project_access_token(self):
        """Test case for get_project_access_token

        Retrieve one token created for this project  # noqa: E501
        """
        pass

    def test_get_project_access_tokens(self):
        """Test case for get_project_access_tokens

        Retrieve all tokens created for this project  # noqa: E501
        """
        pass

    def test_get_project_creator_visas(self):
        """Test case for get_project_creator_visas

        List visas created by user  # noqa: E501
        """
        pass

    def test_get_project_dms_tree(self):
        """Test case for get_project_dms_tree

        Retrieve the complete DMS tree  # noqa: E501
        """
        pass

    def test_get_project_invitations(self):
        """Test case for get_project_invitations

        Retrieve all pending invitations in the project  # noqa: E501
        """
        pass

    def test_get_project_size(self):
        """Test case for get_project_size

        Get size of all model files in the project  # noqa: E501
        """
        pass

    def test_get_project_sub_tree(self):
        """Test case for get_project_sub_tree

        Retrieve the complete projects tree of the cloud  # noqa: E501
        """
        pass

    def test_get_project_tree(self):
        """Test case for get_project_tree

        Retrieve the complete DMS tree  # noqa: E501
        """
        pass

    def test_get_project_users(self):
        """Test case for get_project_users

        Retrieve all users in a project, or a list with a filter by email  # noqa: E501
        """
        pass

    def test_get_project_validator_visas(self):
        """Test case for get_project_validator_visas

        List visas where user is a validator  # noqa: E501
        """
        pass

    def test_get_projects(self):
        """Test case for get_projects

        Retrieve all projects  # noqa: E501
        """
        pass

    def test_get_self_projects(self):
        """Test case for get_self_projects

        List current user's projects  # noqa: E501
        """
        pass

    def test_get_self_user(self):
        """Test case for get_self_user

        Get info about the current user  # noqa: E501
        """
        pass

    def test_get_tag(self):
        """Test case for get_tag

        Retrieve a tag  # noqa: E501
        """
        pass

    def test_get_tags(self):
        """Test case for get_tags

        Retrieve all tags  # noqa: E501
        """
        pass

    def test_get_validation(self):
        """Test case for get_validation

        Retrieve a validation to a visa  # noqa: E501
        """
        pass

    def test_get_validations(self):
        """Test case for get_validations

        List all validations to a visa  # noqa: E501
        """
        pass

    def test_get_visa(self):
        """Test case for get_visa

        Retrieve a visa of a document  # noqa: E501
        """
        pass

    def test_get_visa_comment(self):
        """Test case for get_visa_comment

        Retrieve a comment  # noqa: E501
        """
        pass

    def test_get_visa_comments(self):
        """Test case for get_visa_comments

        List all comment of a visa  # noqa: E501
        """
        pass

    def test_get_visas(self):
        """Test case for get_visas

        List all visas of a document  # noqa: E501
        """
        pass

    def test_invite_cloud_user(self):
        """Test case for invite_cloud_user

        Invite a cloud administrator  # noqa: E501
        """
        pass

    def test_invite_project_user(self):
        """Test case for invite_project_user

        Invite a project member  # noqa: E501
        """
        pass

    def test_leave_project(self):
        """Test case for leave_project

        Leave the project  # noqa: E501
        """
        pass

    def test_make_head_version_document_history(self):
        """Test case for make_head_version_document_history

        Make the head of the version  # noqa: E501
        """
        pass

    def test_pause_visa(self):
        """Test case for pause_visa

        Pause a visa of a document  # noqa: E501
        """
        pass

    def test_reset_validation(self):
        """Test case for reset_validation

        Reset a validation  # noqa: E501
        """
        pass

    def test_resume_visa(self):
        """Test case for resume_visa

        Resume a visa of a document  # noqa: E501
        """
        pass

    def test_update_classification(self):
        """Test case for update_classification

        Update some fields of a classification  # noqa: E501
        """
        pass

    def test_update_cloud(self):
        """Test case for update_cloud

        Update some fields of a cloud  # noqa: E501
        """
        pass

    def test_update_cloud_user(self):
        """Test case for update_cloud_user

        Change the user role in the cloud  # noqa: E501
        """
        pass

    def test_update_document(self):
        """Test case for update_document

        Update some fields of the document  # noqa: E501
        """
        pass

    def test_update_folder(self):
        """Test case for update_folder

        Update some fields of a folder  # noqa: E501
        """
        pass

    def test_update_group_folder(self):
        """Test case for update_group_folder

        Update the permission of a group on a folder  # noqa: E501
        """
        pass

    def test_update_manage_group(self):
        """Test case for update_manage_group

        Update some fields of a group  # noqa: E501
        """
        pass

    def test_update_project(self):
        """Test case for update_project

        Update some fields of a project  # noqa: E501
        """
        pass

    def test_update_project_access_token(self):
        """Test case for update_project_access_token

        Update some fields of a token  # noqa: E501
        """
        pass

    def test_update_project_user(self):
        """Test case for update_project_user

        Change the user role in the cloud  # noqa: E501
        """
        pass

    def test_update_tag(self):
        """Test case for update_tag

        Update some fields of the tag  # noqa: E501
        """
        pass

    def test_update_validation(self):
        """Test case for update_validation

        Update the validator of validation  # noqa: E501
        """
        pass

    def test_update_visa(self):
        """Test case for update_visa

        Update some fields of a visa  # noqa: E501
        """
        pass

    def test_update_visa_comment(self):
        """Test case for update_visa_comment

        Update some fields of a comment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
