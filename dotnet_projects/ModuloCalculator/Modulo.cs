// See https://aka.ms/new-console-template for more information
//A simple application to calculate modulus 
Console.WriteLine("Input num1");
int num1 = System.Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Input num2");
int num2 = System.Convert.ToInt32(Console.ReadLine());
int result = num1 % num2;
Console.WriteLine($"Remainder is: {result}");