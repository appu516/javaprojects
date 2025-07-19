public class studentinfo{
string name;
int roll no;
int age;
void display()
{
    System.out.println("student"+name +"has roll no"+roll no);

}    
}

class student main { 
    public static void main(string args[]){
        studentinfo abc=new studentinfo();
        abc.name="bharath";
        abc.age=56;
        abc.roll no=89;
        abc.display();
    } 

    
}