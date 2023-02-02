Adds new group to be able to create, edit or delete contacts.

Some models actually changes some Contacts values (e.g. a RFQ),
so for ``write`` operations a field exception list is allowed.
This list could be simply altered inheriting from 
``_fields_change_exceptions()`` method for ``res.partner``.
