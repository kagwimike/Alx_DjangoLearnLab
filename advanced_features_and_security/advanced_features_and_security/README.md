# Managing Permissions and Groups in Django

## Overview
This app demonstrates custom permissions and role-based access control using Django Groups.

## Custom Permissions
Defined in Book model:

- can_view
- can_create
- can_edit
- can_delete

These permissions are created using Django's Meta class.

## Groups Created

1. Editors
   - can_view
   - can_create
   - can_edit

2. Viewers
   - can_view

3. Admins
   - can_view
   - can_create
   - can_edit
   - can_delete

## Permission Enforcement

Views are protected using:

@permission_required('advanced_features_and_security.can_edit', raise_exception=True)

If a user does not have permission, a 403 error is raised.

## Testing

Test users were created and assigned to groups to verify permission enforcement.
