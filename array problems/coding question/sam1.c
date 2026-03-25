#include<stdio.h>
void main(){
    int inp=2321054;
    int a[20],b[20],j=0,i,len=0,temp,temp2;
    while(inp>0)
    {
        i=inp%10;
        len++;
        a[j]=i;
        j++;
        inp=inp/10;
    }
    /*for(int i=0;i<len;i++)
    {
        printf("%d",a[i]);
    }
    printf("%d",len);*/

    for(int i=0;i<len;i++)
    {
        for(int j=i+1;j<len;j++)
        {
            if (a[i]>a[j])
            {
                temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }
        }
    }
    for(int i=0;i<len;i++)
    {
        if(a[i]==0){
            temp2=i;
        }
        printf("%d",a[i]);
    }
    
}