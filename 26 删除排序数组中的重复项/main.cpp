#include <vector>
#include <iostream>
#include<algorithm>
using namespace std;

int removeDuplicates(vector<int>& nums) {
	int length = nums.size();
	sort(nums.begin(), nums.end());
	int i = 1;
	while (i < length) {
		if (nums[i] == nums[i - 1]) {
			nums.erase(nums.begin() + (i - 1));
			length--;
			continue;
		}
		i++;
	}
	return nums.size();
}


int main()
{
	vector<int> nums{ 1, 2, 1, 1, 3, 1 };

	int length = removeDuplicates(nums);
	cout << length << endl;
	system("pause");
	return 0;
}