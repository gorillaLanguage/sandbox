namespace cs{
    class Program{
        static void Main(string[] args){
            Console.WriteLine("Hello");

            day d = day.Sunday;

            switch (d)
            {
                case day.Sunday:
                    Console.WriteLine(day.Sunday);
                default:
                    Console.WriteLine("default");
            }

            cs.sub subbbb = new sub();
            subbbb.setStr("これ");
            subbbb.print();
        }
    }

    class sub{
        private string str = "";

        public void setStr( string a){
            str = a;
        }

        public string getStr(){
            return str;
        }

        public void print(){
            Console.WriteLine(str);
        }
    }

    enum day{
    Sunday,
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday
    }
}


// See https://aka.ms/new-console-template for more information
//Console.WriteLine("Hello, World!");
// https://docs.microsoft.com/ja-jp/dotnet/core/tutorials/with-visual-studio-code?pivots=dotnet-6-0
