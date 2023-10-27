#include <iostream>
#include <fstream>
using namespace std;

int main() {

    // Saver files.
    ofstream myfile ("output.txt");

    // Constants.
    //double da = 0.1; // Age compartment "size".
    //double dt = 0.1; // Timestep.
    int nsteps = 1000; // Total number of steps to run.
    
    int Amax = 100; // Number of age compartments.
    int Aadult = 5; // Age of adulthood.
    double M = 0; // Population "biomass".

    // Preallocation.
    double     p[Amax]; // Store for pop. size outputs.
    double ptemp[Amax]; // Store for t=t-1 population.
    double     r[Amax]; // Store for reproduction rates.
    double     m[Amax]; // Store for mortality rates.

    for(int a=0;a<Amax;a++){p[a]=0;ptemp[a]=0;r[a]=0;m[a]=0;} // Set arrays to 0, prevent errors.

    // Initial conditions.
    p[0] = 10; // Set initial population (all eggs).
    myfile << p[0] << ' '; // output population to file.
    for(int a=1;a<Amax;a++){ // Loop over age compartments.
            p[a] = 0; // Set all other age compartments to 0.
            ptemp[a]=0; // Saftey check the "old" compartment store.
            myfile << p[a] << ' '; // Output population to file.
        }
    myfile << endl; // Newline to tidy.

    // Set dynamics functions.
    for(int a=0;a<Amax;a++){ // Loop over age compartments for BVP.
        if (a >= Aadult) {r[a] = 6.9/double(a);} else {r[a]=0;} // Repro. rate.
        if (a >= Aadult) {m[a] = double(a)/10;} else {m[a]=0;} // Mortality.
    }

    // Main Loop.
    for (int t=1;t < nsteps; t++){ // Loop over timesteps.
        for(int a=0;a<Amax;a++){ // Loop over age compartments for BVP.
            ptemp[a] = p[a];
        }

        // Age 0 boundary condition.
        p[0] = 0;
        for(int a=1;a<Amax;a++){ // Loop over age compartments for BVP.
            p[0] += r[a]*ptemp[a]; // New eggs.
        }
        myfile << p[0] << ' '; // output results.

        for(int a=1;a<Amax;a++){ // Loop over age compartments.
            p[a] += ptemp[a-1] - ptemp[a]; // Age population.
            p[a] -= m[a]*p[a]; // Calculate population size.
            if(p[a]<0.005){p[a]=0;} // Clean outputs...
            myfile << p[a] << ' '; // output results.
        }
        myfile << endl;
    }

    myfile.close(); // Close output file.
    return 0; // Terminate script.
}