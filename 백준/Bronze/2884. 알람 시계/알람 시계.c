int main()
{
	int hour = 0;
	int minute = 0;

	scanf("%d", &hour);
	scanf("%d", &minute);

	
	minute -= 45;
		if (minute < 0) {
			hour -= 1;
			minute = 60 + minute;

			if (hour < 0) {
				hour = 24 + hour;
			}
		}


	printf("%d %d", hour, minute);

}