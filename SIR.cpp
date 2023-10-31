#include <QApplication>
#include <QChartView>
#include <QLineSeries>
#include <QValueAxis>
#include <QWidget>

using namespace QtCharts;

/**
 * @brief This program simulates the SIR (Susceptible-Infected-Recovered) model using Qt Charts.
 * 
 * The SIR model is a simple mathematical model used to understand the spread of infectious diseases. 
 * It assumes that the population is divided into three groups: susceptible, infected, and recovered. 
 * The model tracks the number of individuals in each group over time. 
 * 
 * This program initializes the number of susceptible, infected, and recovered individuals, 
 * as well as the infection rate, recovery rate, time step, and number of time steps to simulate. 
 * It then calculates the number of individuals in each group at each time step using the SIR model equations. 
 * Finally, it displays the results using a Qt Chart.
 * 
 * @param argc Number of command line arguments.
 * @param argv Array of command line arguments.
 * @return int Exit status of the program.
 */
int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    QLineSeries *seriesS = new QLineSeries();
    QLineSeries *seriesI = new QLineSeries();
    QLineSeries *seriesR = new QLineSeries();

    double S = 999.0; // initial number of susceptible individuals
    double I = 1.0; // initial number of infected individuals
    double R = 0.0; // initial number of recovered individuals
    double N = S + I + R; // total population
    double beta = 0.3; // infection rate
    double gamma = 0.1; // recovery rate
    double dt = 0.01; // time step
    int nsteps = 10000; // number of time steps to simulate

    for (int i = 0; i < nsteps; i++) {
        double dSdt = -beta * S * I / N;
        double dIdt = beta * S * I / N - gamma * I;
        double dRdt = gamma * I;

        S += dSdt * dt;
        I += dIdt * dt;
        R += dRdt * dt;

        seriesS->append(i*dt, S);
        seriesI->append(i*dt, I);
        seriesR->append(i*dt, R);
    }

    QChart *chart = new QChart();
    chart->addSeries(seriesS);
    chart->addSeries(seriesI);
    chart->addSeries(seriesR);
    chart->setTitle("SIR Model");
    chart->createDefaultAxes();
    chart->axisX()->setTitleText("Time");
    chart->axisY()->setTitleText("Number of Individuals");

    QChartView *chartView = new QChartView(chart);
    chartView->setRenderHint(QPainter::Antialiasing);

    QWidget window;
    window.setCentralWidget(chartView);
    window.resize(800, 600);
    window.show();

    return app.exec();
}
