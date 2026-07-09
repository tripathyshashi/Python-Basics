#include<stdio.h>
int earn;
double fee;
void ability();
int main()
{
    int sem,sub,lec,lecdur,lab,labdur;
    double tlec,tlab,thr,tmin,tsec,tdur,fph,fpm,fps;
    printf("Enter total semesters : ");
    scanf("%d",&sem);
    printf("Enter subjects per semesters : ");
    scanf("%d",&sub);
    printf("Enter lectures per subject : ");
    scanf("%d",&lec);
    printf("Enter duration of each lecture in minutes : ");
    scanf("%d",&lecdur);
    printf("Enter labs per semesters : ");
    scanf("%d",&lab);
    printf("Enter duration of lab lectures per semesters in hours : ");
    scanf("%d",&labdur);
    printf("Enter total fee for all semesters : ");
    scanf("%lf",&fee);
    tlec=sem*sub*lec*lecdur;  //total lecture duration in mins
    tlab=sem*lab*labdur*60;          //total lab duration in mins
    tmin=tlec+tlab;           //overall time spent in mins
    thr=tmin/60;              //overall time spent in hours
    tsec=tmin*60;             //overall time spent in seconds
    fph=fee/thr;              //fee per hours
    fpm=fee/tmin;             //fee per mins
    fps=fee/tsec;             //fee per seconds
    
    printf("\n\t====Analysis====");
    printf("\nTotal semesters : %d",sem);
    printf("\nSubjects per semesters : %d",sub);
    printf("\nLectures per subject : %d",lec);
    printf("\nTotal time spent(in minutes) on lectures : %.2lf",tlec);
    printf("\nLabs per semester : %d",lab);
    printf("\nLab duration of each lab in hours : %d",labdur);
    printf("\nTime spent in lab in minutes : %.2lf\n",tlab);
    
    printf("\n\t===Total study time===");
    printf("\nHours : %.2lf",thr);
    printf("\nMinutes : %.2lf",tmin);
    printf("\nSeconds : %.2lf\n",tsec);
    
    printf("\n\t====Fee Analysis====");
    printf("\nTotal fee for whole semesters : %lf",fee);
    printf("\nFee per hour : %.2lf",fph);
    printf("\nFee per minutes : %.2lf",fpm);
    printf("\nFee per seconds : %.4lf\n",fps);
    
    printf("\nRequirement of money to be earn by parents for fee excluding other expenses :");
    printf("\nPer hour : INR %.2lf",fph);
    printf("\nPer minute : INR %.2lf",fpm);
    printf("\nPer seconds : INR %.4lf\n",fps);
    printf("\nPer Semester : INR %.2lf",fee/sem);
    printf("\nPer Month : INR %.2lf",fee/48);
    ability();
    return 0;
}
void ability()
{
        printf("\n\t===Abilty===\n");
    printf("\nEnter your Earning per month : ");     //Excluding other expenses
    scanf("%d",&earn);
    int res=(int)fee/48;
    printf("\n%d", res);
    if (res<earn)          //minimum 12084 for my fee structure and that even excluding other expenses
    {
    
    printf("\tYour ward is able to get admission to pay off for your expectations");
    }
    else
    printf("\tYou're not able to get admission");
}

    
