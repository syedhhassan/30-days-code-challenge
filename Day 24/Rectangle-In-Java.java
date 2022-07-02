import java.awt.*;
import javax.swing.*;

public class rectangle extends JApplet {

	public void init()
	{
		setSize(400, 400);
		repaint();
	}

	public void paint(Graphics g)
	{
		g.setColor(Color.blue);
		g.drawRect(100, 100, 200, 200);
	}
}