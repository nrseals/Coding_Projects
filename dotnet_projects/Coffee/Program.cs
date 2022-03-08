// See https://aka.ms/new-console-template for more information
// The ideal grounds to water ratio is 2 tbs to 6floz (10g to 180mL)
Console.WriteLine("Welcome! This program will take the guesswork out of brewing coffee in a drip brewer, pour-over, or french press");
Console.WriteLine("Tell me how many cups of coffee you'd like to brew!");
int cups = System.Convert.ToInt32(Console.ReadLine());
// assuming the average cup is 8flOz (237mL) . . .
int water = cups * 8;
int grounds = 2 * (water/6);
Console.WriteLine($"If you need {cups} cups of coffee, you'll want {water} flOz of water and {grounds} tablespoons of grounds. If you're using the metric system, you'll want {Math.Floor(water * 29.574)} mL of water and {Math.Floor(grounds * 14.3)} grams of coffee");

