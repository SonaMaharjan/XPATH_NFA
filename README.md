# XPATH_NFA

## NFA implementation for XPath expressions 

Theory of Computation: Project

## XML Document Example:

	<toc>
		<student>
			<name> sona </name
			<phone> 9849103183 </phone		
			<address> nepal </address>		
		</student	
		<student>	
			<name> rathi </name
			<phone> 9841623722 </phone
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
