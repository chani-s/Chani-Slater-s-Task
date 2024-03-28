import java.net.URL;
import java.util.ResourceBundle;

import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.control.*;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Pane;
import javafx.scene.layout.VBox;

/**
 * @author Chana Slater
 * This is a controller for the Twitter Tower Shape Search.
 */

public class ProjectController implements Initializable{


    @FXML
    private VBox header;

    @FXML
    private Button backToBase;

    @FXML
    private HBox sizeBox;

    @FXML
    private VBox basicPane;

    @FXML
    private AnchorPane buttonsBox;

    @FXML
    private Label rectText;

    @FXML
    private TextField height;

    @FXML
    private TextField width;

    @FXML
    private Button acceptRectangle;

    @FXML
    private Button acceptTriangle;

    @FXML
    private Button triangleScope;

    @FXML
    private Button trianglePrint;

    @FXML
    private Label triangleText;

    @FXML
    private Pane trianglePane;

    // Set the shapes as globals:
    private Triangle tri;
    private Rect rect;

    @FXML
    public void initialize(URL location, ResourceBundle resources) {
        // Set the main window:
        setVisibility(sizeBox, false);
        setVisibility(buttonsBox, false);
        setVisibility(trianglePane, false);
    }

    @FXML
    void rectangle(javafx.event.ActionEvent event) {
        // Set Scene in order to get the rectangle sizes
        setChoosingSize();
        acceptRectangle.setVisible(true);
        backToBase.setVisible(true);
        setVisibility(header, false);
    }

    @FXML
    void triangle(ActionEvent event) {
        // Set Scene in order to get the triangle sizes
        setChoosingSize();
        acceptTriangle.setVisible(true);
        backToBase.setVisible(true);
        setVisibility(header, false);
    }

    @FXML
    void getRectSize(ActionEvent event) {
        Rect rect = new Rect(Double.parseDouble(height.getText()), Double.parseDouble(width.getText()));
        width.clear();
        height.clear();
        // Check the difference between the sizes and print the required calculation
        if(Math.abs(rect.getWidth() - rect.getHeight()) > 5)
            rectText.setText("Area of rectangle: " + rect.getArea());
        else
            rectText.setText("Perimeter of rectangle: " + rect.getPerimeter());
        rectText.setVisible(true);
    }

    @FXML
    void getTriSize(ActionEvent event) {
        tri = new Triangle(Double.parseDouble(height.getText()),Double.parseDouble(width.getText()));
        // Set the options for triangle:
        setVisibility(trianglePane, true);
        triangleText.setText("Your triangle's sizes:\n Height: " + tri.getHeight() + ", Width: "+ tri.getWidth());
        width.clear();
        height.clear();
    }


    private void setChoosingSize()
    {
        // Visible the text fields in order to get the sizes
        setVisibility(sizeBox, true);
        setVisibility(basicPane, false);
    }

    private void setVisibility(Pane parentPane, Boolean bool)
    {
        for (Node node : parentPane.getChildren()) {
            // Set the visibility of each node to false
            node.setVisible(bool);
        }
    }

    @FXML
    void goToBase(ActionEvent event) {
        // Set the window as the start window
        setVisibility(basicPane, true);
        setVisibility(sizeBox, false);
        setVisibility(buttonsBox, false);
        setVisibility(trianglePane, false);
        setVisibility(header, true);
        rectText.setText("");
        triangleText.setText("");
    }

    @FXML
    void onExitClick(ActionEvent event) {
        Platform.exit();
    }

    public void calcTrianglePerimeter(ActionEvent actionEvent) {
        // Print the triangle perimeter
        triangleText.setText("Triangle Perimeter is: " + tri.getPerimeter());
    }


    public void makeTrianglePrint(ActionEvent actionEvent){
        // Check if possible to print the triangle
        if(tri.getWidth() % 2 == 0 || tri.getWidth() > tri.getHeight()*2) {
            triangleText.setText("Impossible to print the triangle.");
        }
        else
            // Print the triangle according to requires
            triangleText.setText(tri.draw());
    }
}




