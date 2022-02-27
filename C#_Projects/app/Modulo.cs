// See https://aka.ms/new-console-template for more information
//A simple application to calculate modulus 
Console.WriteLine("Input num1");
string num1S = Console.ReadLine();
Console.WriteLine("Input num2");
string num2S = Console.ReadLine();
int num1 = System.Convert.ToInt32(num1S);
int num2 = System.Convert.ToInt32(num2S);
int result = num1 % num2;
Console.WriteLine($"Remainder is: {result}");
