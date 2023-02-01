using System;

class Pyramid
{
    #region problem_explanation
    /*
     * Escriba un método que muestre en pantalla la pirámide de asteriscos
     * mostrada a continuación, usando únicamente recursividad (nada de ciclos):
     *              *
     *             * *
     *            * * *
     *           * * * *
     *          * * * * *
     *         * * * * * *
     *        * * * * * * *
     *       * * * * * * * *
     *      * * * * * * * * *
    */
    #endregion

    #region global_variables
    /*
     * Variables que nos dictan los intervalos inferior y
     * superior donde se imprimiran los asteriscos en cada
     * nivel de la piramide 
    */
    private static int lowEndpoint;
	private static int topEndpoint;
    #endregion

    public static void Main()
    {
        PrintPyramidRecursive(1, 9, 0, false);
    }

    #region functionality
    // Método principal recursivo, imprime el siguiente caractér en la actual fila 'layer'
    // layer: la capa de la piramide que se está imprmiendo, 1 = punta de la pirámide, height = base de la pirámide
    // height: la altura deseada de la pirámmide
    // index: el índice del actual caracter que se va a imprimir en pantalla de la fila 'layer'
    // preWasStar: booleano que indica si el caractér previo fue un asterisco
    private static void PrintPyramidRecursive(int layer, int height, int index, bool prevWasStar)
    {
        // Si hemos excedido la altura de la pirámide, terminamos
        if(layer > height)
            return;

        // Si iniciamos un nuevo nivel de la pirámide, calculamos sus intervalos
		if(index == 0)
			CalculateEndpoints(layer, height);

        bool inInterval = index >= lowEndpoint && index < topEndpoint;
        if(inInterval)
		{
            /*
             * Si el caracter previo fue un asterisco, imprimir un
             * espacio en blanco, de lo contrario se imprime un 
             * asterisco; esto es para darle estética a la salida
            */
			if(prevWasStar)
			{
            	Console.Write(" ");
				prevWasStar = false;
			}
			else
			{
				Console.Write("*");
				prevWasStar = true;
			}
		}
        else
            Console.Write(" ");
        
        bool endOfLayer = index >= topEndpoint;
        if(endOfLayer)
        {
            layer++;
            index = 0;
			prevWasStar = false;
            Console.WriteLine("");
        }
        else
            index++;

        // Llamamos al siguiente caracter a imprirse
        PrintPyramidRecursive(layer, height, index, prevWasStar);
    }

    // Método auxiliar para calcular el intervalo donde se imprimen los asteriscos
	public static void CalculateEndpoints(int layer, int height)
	{
        /*
         * lowEndpoint = height - layer = 9 - 1 = 8
         *       |------|
         *      -12345678*
         *      -       * *
         *      -      * * *
         *      -lowE-1234567 = lowEndpoint + (2 * layer) - 1 = 5 + (2 * 4) - 1 = 7 
         *      -     * * * *
         *      -    * * * * *
         *      -   * * * * * *
         *      -  * * * * * * *
         *      - * * * * * * * *
         *      -* * * * * * * * *
        */
		lowEndpoint = height - layer;
        topEndpoint = lowEndpoint + (2 * layer) - 1;
	}
    #endregion
}