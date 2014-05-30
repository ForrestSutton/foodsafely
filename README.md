foodsafely
==========

a python google app engine implementation of a food safely system 

#to do
create models for items, facilities
make sure that items process can pull info from the facities

tables "items", "facility"
    string   "code"
    integer  "facility_id"
    boolean  "peanuts"
    boolean  "tree_Nuts"
    boolean  "eggs"
    boolean  "dairy"
    boolean  "wheat_gluten"
    boolean  "soy"
    boolean  "fish"
    boolean  "crusta"
    string   "same_Line"
    string   "certifications"
    string   "item_class"
    datetime "updated_at"
