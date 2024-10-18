import java.util.Scanner; // bring classes from java library
   public class NegativeAndPositive{ // declare a public class name
      public static void main(String[] args){
 // the main method begins excution of java application
         Scanner input = new Scanner(System.in);
 // creating scanner input

            System.out.print("Enter first Number: ");
 // prompt user to enter firstNumber
            int num1 = input.nextInt(); 
// read the first number

         System.out.print("Enter second Number: ");
 //prompt user to enter secondNumber
         int num2 = input.nextInt();
 //read the secondnumber


        System.out.print("Enter thirdNumber: ");
 //prompt user to enter third Number
       int num3 = input.nextInt();
 
//read the thirdnumber


System.out.print("Enter forth Number: ");
 //prompt user to enter forthNumber
int num4 = input.nextInt(); 
//read the forthnumber

System.out.print("Enter fifth Number: ");
 //prompt user to enter fifthNumber
int num5 = input.nextInt(); 
//read the fiftnumber


if(num1>0){ 
//check if num1 is greater than zero
System.out.println("Number is Positive");
 //executes if num1 is positive

}else if(num1<0){
 //check if num1 is less than zero
System.out.println("Number is Negetive");
 //executes if num1 is negative

}else{ 
//if num1 is neither positive nor negative
System.out.println("Number is Zero"); 
//executes if num1 is zero

}
if(num2>0){ //check if num2 is greater than zero
System.out.println("Number is Positive");
 //executes if num2 is positive

}else if(num2<0){ //check if num2 is less than zero 
System.out.println("Number is Negetive");
 //executes if num2 is negative

}else{ //if num2 is neither positive nor negative
System.out.println("Number is Zero"); 
//executes if num2 is zero

}
if(num3>0){
 //check if num3 is greater than zero
System.out.println("Number is Positive"); 
 //executes if num3 is positive

}else if(num3<0){ //check if num3 is less than zero
System.out.println("Number is Negetive");
 //executes if num3 is negative

}else{ 
//if num3 is neither positive nor negative
System.out.println("Number is Zero");
 //executes if num3 is zero

}
if(num4>0){
 //check if num4 is greater than zero
System.out.println("Number is Positive");
 //executes if num4 is positive

}else if(num4<0){ 
//check if num4 is less than zero
System.out.println("Number is Negetive");
 //executes if num4 is negative

}else{ //if num4 is neither positive nor negative
System.out.println("Number is Zero");
 //executes if num4 is zero

}
if(num5>0){ 
//check if num5 is greater than zero
System.out.println("Number is Positive");
 //executes if num5 is positive

}else if(num5<0){
 //check if num5 is less than zero
System.out.println("Number is Negetive");
 //executes if num5 is negative

}else{ 
//if num5 is neither positive nor negative
System.out.println("Number is Zero");
 //executes if num5 is zero
}
}
} 