public class Rect extends Shape{
    public Rect(double height, double width)
    {
        super(height, width);
    }

    public double getPerimeter()
    {
        return this.getHeight()*2 + this.getWidth()*2;
    }

    public double getArea()
    {
        return this.getHeight()*this.getWidth();
    }

    public String draw()
    {
        return "";
    }

}
