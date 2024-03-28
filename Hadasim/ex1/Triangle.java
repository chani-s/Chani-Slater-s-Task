public class Triangle extends Shape{
    public Triangle(double height, double width)
    {
        super(height, width);
    }


    public double getPerimeter()
    {
        double sideLength = Math.sqrt(Math.pow(this.getWidth() / 2, 2) + Math.pow(this.getHeight(), 2));
        double perimeter = 2 * sideLength + this.getWidth();
        return perimeter;
    }

    public String draw() {
        String triangle = "*\n"; // the top of triangle
        int numOfStars = 3; // number of stars of each line. starts with 3.
        int numOfSameLength = (int)(this.getHeight()-2)/(int)((this.getWidth()-2)/2); // number of lines in the same length
        int extra = (int)(this.getHeight()-2)%(int)((this.getWidth()-2)/2); // number of extra lines in the top (when needed extra)
        //Print the top section as needed
        for (int i = 0; i < extra; i++) {
            triangle += "***\n";
        }
        //Print the body of the triangle
        for (int i = 1; i < this.getHeight() && numOfStars < this.getWidth(); i++) {
            for (int j = 0; j < numOfSameLength; j++) {
                int counter = numOfStars;
                while (counter > 0) {
                    triangle += "*";
                    counter--;
                }
                triangle += "\n";
            }
            numOfStars += 2;
        }
        //Print the bottom line:
        for (int i = 0; i < this.getWidth(); i++)
            triangle += "*";
        return triangle;
    }



}
