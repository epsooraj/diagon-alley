# The Diagon Alley

Django E-Commerce Server Base

## Product

Product app manages CRUD of products.
It is embeded with Units in with the concept as all products will have units. The products without units are also added to the units with values of 'unit' and 'value' as None. (ie, All products will have a minimum of one unit).

### Database

Product app has a database table named 'products' with the following columns:

#### Product

| Column | Type | Description |
| ------ | ------ | ----------- |
| id | integer | Unique identifier for the product |
| name | char[255] | Name of the product |
| name_2 | char[255] | Alternate name/ Name in 2nd language |
| description | text | Description of the product |
| category | foreign key | Foreign key to the category table |
| sub_category | foreign key | Foreign key to the category table |
| created_at | datetime | Date and Time in which the product is created |
| update_at | datetime | Date and Time of the last update |

#### Unit
| Column | Type | Description |
| ------ | ------ | ----------- |
| id | integer | Unique identifier for the unit |
| product | foreign key | Foreign key to the product table |
| unit | char[255] | Name of the unit. eg: kg, g |
| value | char[255] | Value of the corresponding unit. eg 2, 34 |
| price | float | Price of the product to corresponding unit |
| discount_percentage | float | Discount Percentage of the product to corresponding unit |
| created_at | datetime | Date and Time in which the unit is created |
| update_at | datetime | Date and Time of the last update |

### Todo

- [x] User
- [x] Category
- [x] Product
- [x] Cart
- [ ] Order
- [ ] Report
