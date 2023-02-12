using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace calcu
{

    public partial class MainWindow : Window
    {
        string number1 = "";
        string number2 = "";
        string operator1 = "";
        public MainWindow()
        {

            InitializeComponent();
        }
        private void button1_Click(object sender, RoutedEventArgs e)
        {
            if (operator1 == "")
            {
                number1 = number1 + 1;
                result.Text = number1.ToString();
            }
            else
            {
                number2 = number2 + 1;
                result.Text = number2.ToString();
            }
        }
        private void button2_Click(object sender, RoutedEventArgs e)
        {
            if (operator1 == "")
            {
                number1 = number1 + 2;
                result.Text = number1.ToString();
            }
            else
            {
                number2 = number2 + 2;
                result.Text = number2.ToString();
            }
        }
        private void button3_Click(object sender, RoutedEventArgs e)
        {
            if (operator1 == "")
            {
                number1 = number1 + 3;
                result.Text = number1.ToString();
            }
            else
            {
                number2 = number2 + 3;
                result.Text = number2.ToString();
            }
        }
        private void button4_Click(object sender, RoutedEventArgs e)
        {
            if (operator1 == "")
            {
                number1 = number1 + 4;
                result.Text = number1.ToString();
            }
            else
            {
                number2 = number2 + 4;
                result.Text = number2.ToString();
            }
        }
        private void button5_Click(object sender, RoutedEventArgs e)
        {
            if (operator1 == "")
            {
                number1 = number1 + 5;
                result.Text = number1.ToString();
            }
            else
            {
                number2 = number2 + 5;
                result.Text = number2.ToString();
            }
        }
        private void button6_Click(object sender, RoutedEventArgs e)
        {
            if (operator1 == "")
            {
                number1 = number1 + 6;
                result.Text = number1.ToString();
            }
            else
            {
                number2 = number2 + 6;
                result.Text = number2.ToString();
            }
        }
        private void button7_Click(object sender, RoutedEventArgs e)
        {
            if (operator1 == "")
            {
                number1 = number1 + 7;
                result.Text = number1.ToString();
            }
            else
            {
                number2 = number2 + 7;
                result.Text = number2.ToString();
            }
        }
        private void button8_Click(object sender, RoutedEventArgs e)
        {
            if (operator1 == "")
            {
                number1 = number1 + 8;
                result.Text = number1.ToString();
            }
            else
            {
                number2 = number2 + 8;
                result.Text = number2.ToString();
            }
        }
        private void button9_Click(object sender, RoutedEventArgs e)
        {
            if (operator1 == "")
            {
                number1 = number1 + 9;
                result.Text = number1.ToString();
            }
            else
            {
                number2 = number2 + 9;
                result.Text = number2.ToString();
            }
        }
        private void button0_Click(object sender, RoutedEventArgs e)
        {
            if (operator1 == "")
            {
                number1 = number1 + 0;
                result.Text = number1.ToString();
            }
            else
            {
                number2 = number2 + 0;
                result.Text = number2.ToString();
            }
        }




        private void buttonplus_Click(object sender, RoutedEventArgs e)
        {
            operator1 = "+";
            result.Text = "0";
        }
        private void buttonmin_Click(object sender, RoutedEventArgs e)
        {
            operator1 = "-";
            result.Text = "0";
        }
        private void buttondiv_Click(object sender, RoutedEventArgs e)
        {
            operator1 = "/";
            result.Text = "0";
        }
        private void buttonmul_Click(object sender, RoutedEventArgs e)
        {
            operator1 = "*";
            result.Text = "0";
        }
        private void buttonequals_Click(object sender, RoutedEventArgs e)
        {
            double number1Double = double.Parse(number1);
            double number2Double = double.Parse(number2);
            switch (operator1)
            {
                case "+":

                    result.Text = (number1Double + number2Double).ToString();
                    number1 = (number1Double + number2Double).ToString();
                    number2 = "";
                    break;
                case "-":
                    result.Text = (number1Double - number2Double).ToString();
                    number1 = (number1Double - number2Double).ToString();
                    number2 = "";
                    break;
                case "*":
                    result.Text = (number1Double * number2Double).ToString();
                    number1 = (number1Double * number2Double).ToString();
                    number2 = "";
                    break;
                case "/":
                    result.Text = (number1Double / number2Double).ToString();
                    number1 = (number1Double / number2Double).ToString();
                    number2 = "";
                    break;
            }
            operator1 = "";

        }
        private void buttonce_Click(object sender, RoutedEventArgs e)
        {
            number1 = "";
            number2 = "";
            operator1 = "";
            result.Text = "0";
        }







    }
}
