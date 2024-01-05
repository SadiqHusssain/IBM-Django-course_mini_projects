you will learn to query and access related objects spanning relationships.

Learning Objectives
Query related objects spanning relationships

Concepts covered in the lab
QuerySet: Represents a collection of records in a database, and is required to read objects using Django Model API.

get() method: Returns a single object that matches the lookup criterion.

all() method: Returns a QuerySet of all the objects in the database.

filter() method: Returns only the rows that match the search term. It can have lookup parameters such as greater than, less than, contains, or is null.

Forward relationship: If a model has a Foreign key, instances of that model will have access to the related (foreign) object via an attribute of the model.

Backward relationship: If a model has a Foreign key, instances of the foreign-key model will have access to a Manager that returns all instances of the first model.