import java.util.Scanner;
interface base1
{
    void info();
}
interface base2
{
    void getdata();
    void calculate();
}
class derived implements base1,base2{
    int eid;
    String name;
    double bp,hra,da,np;
    public void info()
    {
        Scanner input=new Scanner(System.in);
        Scanner in=new Scanner(System.in);
        System.out.println("Enter Employee ID:");
        eid =input.nextInt();
        System.out.println("Enter the employee name:");
        name=in.nextLine();
    }
    public void getdata()
    {
        Scanner in=new Scanner(System.in);
        System.out.println("Enter basic pay:");
        bp=in.nextDouble();
        da=bp*0.4;
        hra=bp*0.1;
    }
    public void calculate()
    {
        np=bp+da+hra;
    }
    void display()
    {
        System.out.println("Employee ID: "+eid);
        System.out.println("Employee Name: "+name);
        System.out.println("Basic Pay: "+bp);
        System.out.println("DA: "+da);
        System.out.println("HRA: "+hra);
        System.out.println("NP: "+np);
    }
}

public class Main{
    public static void main(String[] args)
    {
        derived obj=new derived();
        obj.info();
        obj.getdata();
        obj.calculate();
        obj.display();
    }
}