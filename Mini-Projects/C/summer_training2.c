//Program to calculate the earning of institution by claculating the fee per student and then entering the number of students
//Date : 11 June 2026
//Programmer : Shashi 


#include<stdio.h>
int earn,sem;
double fee,fpl;
void ability();
void amount();
int main()
{
    int sub,slec,llec,dur,lab;
    double tlec,tlab,tmin,fpm,fph;
    double cf=fee*4;
    printf("Enter total semesters : ");
    scanf("%d",&sem);
    printf("Enter subjects per semesters : ");
    scanf("%d",&sub);
    printf("Enter lectures per subject : ");
    scanf("%d",&slec);
    printf("Enter Labs per semesters : ");
    scanf("%d",&lab);
    printf("Enter Lecture per Lab : ");
    scanf("%d",&llec);
    printf("Enter duration of each lecture in minutes : ");
    scanf("%d",&dur);
    printf("Fee per year : ");
    scanf("%lf",&fee);
    cf=fee*4;
    printf("\nFee for the course : INR %.2lf\n",cf);
    tlec=sem*sub*slec*dur;          //total lecture duration in mins
    tlab=sem*lab*llec*dur;          //total lab duration in mins
    tmin=tlec+tlab;                 //overall time spent in mins
    fpm=fee/tmin;                   //fee per mins
    fph=fpm*60;
    fpl=fpm*50;
    
    printf("\n\t\t====Analysis====");
    printf("\nTotal semesters : %d\t\tSubjects : %d\tLabs : %d",sem,sub,lab);
    printf("\nLectures per subject : %d\tLecture per Lab : %d",slec,llec);
    printf("\nTime spent in lectures : %.2lf mins",tlec);
    printf("\nTime spent in lab :      %.2lf mins\n",tlab);
    //printf("\nDuration of each lecture in minutes : %d",dur);
    
    printf("\nTotal study time :  %.2lf Minutes\n",tmin);
    
    printf("\n\t\t====Fee Analysis====");
    printf("\nFee for a year:   INR %.2lf",fee);
    printf("\nFee per minutes : INR %.2lf\n",fpm);
    
    printf("\nRequirement of money to be earn by parents for fee excluding other expenses :\n");
    printf("\nPer Minute :      INR %.2lf",fpm);
    printf("\nFee per lecture : INR %.2lf",fpm*50);
    printf("\nPer Hour :        INR %.2lf",fph);
    printf("\nPer Semester :    INR %.2lf",fee/2);
    printf("\nPer Month :       INR %.2lf\n",fee/12);
    amount();
    ability();
    return 0;
}
void ability()
{
        printf("\n\t===Abilty===\n");
    printf("\nEnter your Earning per month : ");     //Excluding other expenses
    scanf("%d",&earn);
    int res=(int)fee/12;
    //printf("\n%d", res);
    if (res<earn)          //minimum 12084 for my fee structure and that even excluding other expenses
    {
    
    printf("\tYour ward is able to get admission to pay off for your expectations");
    }
    else
    printf("\tYou're not able to get admission");
}
void amount()
{
    int spc,lecpd,earnpl,earnpd,tc;
    double tepd,teps,tedc;
    //tepd=tc*fpl*60*8;
    //teps=tc*fpl*60*8*90;
    //tedc=sem*tc*fpl*60*8*90;
    printf("\n\t\t====AMOUNT EARNED BY INSTITUTION====\n");
    printf("\nEnter the no. of students in a class : ");
    scanf("%d",&spc);
    printf("\n\t===EARNING PER STUDENT===");
    printf("\nIn a lecture : INR %.2lf",fpl);
    printf("\nIn a day :     INR %.2lf",fpl*8);
    //printf("\nIn a semester :INR %.2lf",fpl*8*90);
    printf("\n\t===EARNING PER CLASS===");
    printf("\nIn a lecture : INR %.2lf",fpl*60);
    printf("\nIn a day :     INR %.2lf",fpl*60*8);
    //printf("\nIn a semester :INR %.2lf\n",fpl*60*8*90);
    printf("\n\t===Total earning===");
    printf("\nEnter total number of classes : ");
    scanf("%d",&tc);
    printf("\nTotal earning in a day :          INR %.2lf",tc*fpl*60*8);
    printf("\nTotal earning in a semester :     INR %.2lf",tc*fpl*60*8*90);
    printf("\nTotal earning during the course : INR %.2lf\n",sem*tc*fpl*60*8*90);
    
}