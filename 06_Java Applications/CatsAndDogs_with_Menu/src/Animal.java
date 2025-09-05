public abstract class Animal {
    private int id;
    private String name;
    private int age;

    // Constructor
    public Animal(int id, String name, int age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }

    // Getters and Setters: with minimal validation
    public int getId() {
        return id;
    }
    public void setId(int id) {
        if (id >= 0) {
        this.id = id;
        } else {
            System.out.println("Invalid ID. ID must be greater than or equal to 0.");
        }
    }

    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = safe(name);
    }

    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        if (age >= 0 && age <= 25) {
            this.age = age;
        } else {
            System.out.println("Invalid age. Age must be between 0 and 25.");
        }
    }

    protected static String safe(String text) {                                                                         // protected, means that it can be used by subclasses or classes from the same package. static, means that belongs to class (Animal.safe("..."))
        return (text == null) ? "" : text.replace(",", " ").trim();                                                                       // uses ternary operator. if the condition text is null, returns "" (an empty string), otherwise returns text.trim(), that is the same text without spaces before and after.
    }

    // Polymorphic  and 2 extra values for CSV to display
    public abstract String type();                                                                                      // for example, "dog" or "cat"

    // 2 optional extras for CSV (they can be empty)
    public abstract String[] extrasForCsv();                                                                            // abstract, does not have a body {...} returns [EXTRA1, EXTRA2]
                                                                                                                        // each subclass must implement this method and decide which extras returns

    // Single source of truth for console and CSV rows
    // CSV: ID, TYPE, NAME, AGE, EXTRA1, EXTRA2
    @Override
    public String toString() {                                                                                          // Method inherited from Object (the superclass of all classes in Java). Method that returns a string that represents the object. When I write System.out.println(myObject), Java calls to String, automatically
        String[] extraFeatures = extrasForCsv();                                                                        // calls the abstract method extrasForCsv() (it is defined by each subclass) and it saves it in an array extraFeatures.

        String extraFeature1 = (extraFeatures != null && extraFeatures.length > 0) ? safe(extraFeatures[0]) : "";             // it makes sure that the array is not null and that there is at least 1 element in the array
                                                                                                                        // if both conditions are fullfilled, then uses the first element extrafeatures[0], otherwise uses "" (empty string)
        String extraFeature2 = (extraFeatures != null && extraFeatures.length > 1) ? safe(extraFeatures[1]) : "";

        return getId() + "," + type().toUpperCase() + "," + getName() + "," + getAge() + "," + extraFeature1 + "," + extraFeature2;
    }

}
