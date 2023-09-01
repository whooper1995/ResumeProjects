/* This program prompts the user to input a date, and will return the day of the week
that, that date occured.  The program starts by finding the day of the week of the same
day in month in 2020.  The program than calculates the number of leap years between the
 2 years and then finds the day of the week for the input date.*/

#include<iostream>

using namespace std;


int main () {
//Define Variables
    char garbage;
    int dayCount;
    int inputYear;
    int inputMonth;
    int inputDay;
    int numOfLeaps=0;
    string outputDay;

//Promts User for date
    cout<<"Input a date in mm/dd/yyyy form: "; 
    cin>>inputMonth>>garbage>>inputDay>>garbage>>inputYear;

//Calculates the day of the week of mm/dd/2020 
    if (inputMonth==1 || inputMonth==4 || inputMonth == 7)
        dayCount=(inputDay+2)%7;
    else if (inputMonth==2 || inputMonth==8)
        dayCount=(inputDay+5)%7;
    else if (inputMonth==3 || inputMonth==11)
        dayCount=(inputDay+6)%7;
    else if (inputMonth==5)
        dayCount=(inputDay+4)%7;
    else if (inputMonth==6)
        dayCount=inputDay%7;
    else if (inputMonth==9 || inputMonth==12)
        dayCount=(inputDay+1)%7;
    else if (inputMonth==10)
        dayCount=(inputDay+3)%7;

//Calculates the number of Leap Years inbetween March 1 2020, and the input date
    numOfLeaps=(inputYear-2020)/4;
    if (inputYear<2020)
        numOfLeaps-=1;
    

//Calculates the day of the week of mm/dd/yyyy
    dayCount=dayCount+(inputYear-2020)+numOfLeaps;
    dayCount=dayCount%7;

//Adjust dayCount to be positive
    if (dayCount<0)
        dayCount+= 7;
    
//Assigns outPutDay
    switch (dayCount)
    {case 0:
        outputDay="Sunday";
        break;
    case 1:
        outputDay="Monday";
        break;
    case 2: 
        outputDay="Tuesday";
        break;
    case 3:
        outputDay="Wednesday";
        break;
    case 4:
        outputDay="Thursday";
        break;
    case 5:
        outputDay="Friday";
        break;
    case 6:
        outputDay="Saturday";
        break;}

//Print output
    cout<<inputMonth<<"/"<<inputDay<<"/"<<inputYear<<" occurs on a "<<outputDay<<"."<<endl;

    return 0;} 


