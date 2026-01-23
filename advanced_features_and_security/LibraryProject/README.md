# Advanced Features and Security

## Permissions and Groups

This project implements role-based access control using Django permissions and groups.

### Custom Permissions
The Book model defines the following custom permissions:
- can_view
- can_create
- can_edit
- can_delete

### Groups
The following groups are used:
- Editors: can_create, can_edit
- Viewers: can_view
- Admins: all permissions

### Views Protection
Django's `@permission_required` decorator is used to restrict access to:
- Creating books
- Editing books
- Deleting books

Only users with the correct permissions can access these actions.
