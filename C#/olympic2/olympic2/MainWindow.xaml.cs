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

namespace olympic2
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>



    public partial class MainWindow : Window
    {
        private readonly CustomCanvas canvas;
        public MainWindow()
        {
            InitializeComponent();
            canvas = new CustomCanvas();
            Content = canvas;
            Loaded += MainWindow_Loaded;

        }

        private void MainWindow_Loaded(object sender, RoutedEventArgs e)
        {
            var button = new Button
            {
                Content = "Update Position"
            };
            button.Click += Button_Click;
            canvas.Children.Add(button);
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            canvas.InvalidateVisual();
        }
    }

    public class CustomCanvas : Canvas
    {
        private Ellipse[] ellipses = new Ellipse[5];
        private Random random = new Random();

        public CustomCanvas()
        {
            for (int i = 0; i < 5; i++)
            {
                ellipses[i] = new Ellipse
                {
                    Width = 100,
                    Height = 100,
                    Fill = i switch
                    {
                        0 => Brushes.Blue,
                        1 => Brushes.Yellow,
                        2 => Brushes.Black,
                        3 => Brushes.Green,
                        4 => Brushes.Red,
                        _ => Brushes.Transparent
                    }
                };
                Children.Add(ellipses[i]);
            }
        }

        protected override void OnRender(DrawingContext drawingContext)
        {
            base.OnRender(drawingContext);
            for (int i = 0; i < 5; i++)
            {
                SetLeft(ellipses[i], random.Next(0, (int)ActualWidth - 100));
                SetTop(ellipses[i], random.Next(0, (int)ActualHeight - 100));
            }
        }
    }
}