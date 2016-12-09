#include "BinaryTree.h"
#include <vector>
#include <iostream>
#include <cmath>

using namespace BinaryTree;

BinaryTree(int root)
{
	vals = new std::vector <int>;
	vals->push_back(new int(root));	
}

~BinaryTree()
{
	clear();
	delete vals;
}

bool isEmpty()
{	return (vals->size() == 0);	}

int getHeight()
{	
	if(vals->size() == 0)
		return 0;
	else if(vals->size() == 1)
		return 1;
	else
		return findHeight();
}

int numNodes()
{	return vals->size();	}

int getRoot()
{	if((vals->size() > 0) && (vals->[0] != nullptr))
		return (*vals)[0];
	else
		return -999;
}

void setRoot(int val)
{
	if(vals->size() > 0)
		(*vals)[0] = new int(val);
	else
		vals->push_back(new int(val));
}

void clear()
{
	for(int i = 0; i < vals->size(); i++)
		if(vals->[i] != nullptr)
			delete (*vals)[i];
}

int getEntry(int val)
{	return (contains(val)) ? val : -999;	}

bool contains(int val)
{
	bool found = false;
	
	for(int i = 0; i < vals->size(); i++)
		if(*((*vals)[i]) == val)
			found = true;
			
	return found;
}

int search(int val, int loc)
{
	if(loc < vals->size())
	{
		if (*(vals->[loc]) == val)
			return loc;
		else if(*(vals->[loc]) > val)
			loc = 2*loc + 1;
			return search(val, loc);
		else
			loc = 2*loc + 2;
			return search(val, loc);
	}
	
	else 
		return loc; 
}

bool add(int val)
{
	addLoc = search(val, 0);
	bool added = false;
	
	if(addLoc = vals->size())
	{
		added = true;
		vals->push_back(new int(val));
	}
	
	else if(addLoc = (vals->size()+1))
	{
		added = true;
		vals->push_back(nullptr);
		vals->push_back(new int(val));
	}
	
	return added;
}

int findHeight()
{	return std::log2(vals->size());	}
