#ifndef BINARYTREE_H
#define BINARYTREE_H

#include <vector>

class BinaryTree
{
	public:
		
		BinaryTree(int root);
		~BinaryTree();
		
		bool isEmpty();
		int getHeight();
		int numNodes();
		int getRoot();
		void setRoot(int val);
		bool add(int val);
		void clear();
		int getEntry( int val);
		bool contains(int val);

	private:
		int findHeight();
		int search(int val);
		std::vector <int*> * vals;
		
};
#endif
