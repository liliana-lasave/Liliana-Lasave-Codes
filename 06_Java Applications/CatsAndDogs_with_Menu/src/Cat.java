// Cat: EXTRA1 = color, EXTRA2 = origin

public class Cat extends Animal {
    private String color;                                                                                               // EXTRA1
    private String origin;                                                                                              // EXTRA2 if it is wild or domesticated



    // Constructor
    public Cat(int id, String name, int age, String color, String origin) {
        super(id, name, age);
        this.color = safe(color);
        this.origin = safe(origin);
    }

    // Getters and Setters
    public String getColor() {
        return color;
    }
    public void setColor(String color) {
        this.color = safe(color);
    }

    public String getOrigin() {
        return origin;
    }
    public void setOrigin(String origin) {
        this.origin = safe(origin);
    }

    // Polymorphic label
    @Override
    public String type() {
        return "CAT";
    }

    // CSV extras (two optional fields)
    @Override
    public String[] extrasForCsv() {

        return new String[]{color, origin};           // String[], without size
    }

}
