using System;

class Printer
{
	static void PrintArray<T>(System.Collections.Generic.IList<T> ToPrint)
    {
        foreach(var x in ToPrint)
        {
            Console.WriteLine(x.ToString());
        }
    }
    /**
	*    Name: PrintArray
	*    Print each element of the generic array on a new line. Do not return anything.
	*    param A generic array
	**/
    // Write your code here

    static void Main(string[] args)
	{
		int n = Convert.ToInt32(Console.ReadLine());
		int[] intArray = new int[n];
		for (int i = 0; i < n; i++)
		{
			intArray[i] = Convert.ToInt32(Console.ReadLine());
		}

		n = Convert.ToInt32(Console.ReadLine());
		string[] stringArray = new string[n];
		for (int i = 0; i < n; i++)
		{
			stringArray[i] = Console.ReadLine();
		}

		PrintArray<Int32>(intArray);
		PrintArray<String>(stringArray);
	}
}