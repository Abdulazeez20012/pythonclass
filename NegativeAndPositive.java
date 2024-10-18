import java.util.Scanner; 
   public class NegativeAndPositive
      public static void main(String[] args){

         Scanner input = new Scanner(System.in);

            System.out.print("Enter first Number: ");
 
            int num1 = input.nextInt(); 

         System.out.print("Enter second Number: ");
 
         int num2 = input.nextInt();

        System.out.print("Enter thirdNumber: ");

       int num3 = input.nextInt();
 
System.out.print("Enter forth Number: ");
int num4 = input.nextInt(); 

System.out.print("Enter fifth Number: ");
 
int num5 = input.nextInt();

if(num1>0){ 

System.out.println("Number is Positive");
 
}else if(num1<0){
 
System.out.println("Number is Negetive");
 
}else{ 

System.out.println("Number is Zero"); 

}
if(num2>0){ 
System.out.println("Number is Positive");
 
}else if(num2<0){ 
System.out.println("Number is Negetive");

}else{ 
System.out.println("Number is Zero"); 

}
if(num3>0){
System.out.println("Number is Positive"); 

}else if(num3<0){
System.out.println("Number is Negetive");

}else{ 
System.out.println("Number is Zero");
}
if(num4>0){

System.out.println("Number is Positive");

}else if(num4<0){ 

System.out.println("Number is Negetive");
 
}else{ 
System.out.println("Number is Zero");

}
if(num5>0){ 

System.out.println("Number is Positive");

}else if(num5<0){
 
System.out.println("Number is Negetive");

}else{ 
System.out.println("Number is Zero");
 
}
}
} 