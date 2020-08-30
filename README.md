# XPATH_NFA

## NFA implementation for XPath expressions 

Theory of Computation: Project

# Description: 

The emergence of XML (Extensible Markup Language) as a data conversion language has led to a proliferation of databases that store, query and update XML data. XML is rapidly being used for the creation and parsing of documents. It allows effective sharing of data and simplify data storage. Along with popularity gained by this language, efficient querying of data i.e. retrieving data from XML documents has been an area of interest for a lot of people.

As a part of my TOC project, I'm presenting an application of NFA for query search in XML Language. 

# Input Format:

The input needs to be a valid x-path expression. Each of the nodes in the path needs to be separated by space. 

For eg: /toc /student /name[text()='sona'] (Note the space between the two location steps)

Invalid: /toc/student/name[text()='sona'] [Invalid because of the incorrect input format. The nodes need to be separated by space]

## XML Document Example:

	<toc>
		<student>
			<name> sona </name
			<phone> 9999999999 </phone		
			<address> nepal </address>		
		</student	
		<student>	
			<name> xyz </name
			<phone> 8888888888 </phone
			<address> india </address>
		</student
	</toc

## Functionality: 
1. To check if the text entered is in the document or not:
- /toc /student /name[text()='sona']
- /toc /student /phone[text()='9999999999']
- /toc /student /name[address()='nepal']

2. Check if the input is a valid path expression or not (/):
- /toc 
- /toc /student
- /toc /student /name
- /toc /student /address
- /toc /student /phone

3. Valid path expression and select all the elements (//):
- //toc
- //student
- //name 
- //phone
- //address
- /toc /student //name
- /toc /student //address
- /toc /student //phone

4. Return the text in the given element (/text() and predicates):
- //student /text()
- /toc /student //name /text()
- /toc /student //phone /text()
- /toc /student //address /text()
- /toc /student[1]
- /toc /student[2]

5. Access all child elements of the given node (/*):
- /toc /*
