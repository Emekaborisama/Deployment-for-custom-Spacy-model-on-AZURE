# Insurwave ML Service code test

## Introduction

Let's imagine you are part of the data science team in a company that specialises in data extraction. The team has been asked to create a solution that can extract dates from text inputs.

Example inputs:
```
Example 1: ‘The policy provides cover from 31st June 2019 to 1st July 2022 inclusive’
Example 2: ‘Policy terms from 1/1/2021 to 31/12/2022’
``` 
Following experimentation with different features and models the data science team has concluded that the best results are obtained by: 

1.	Removing special characters from input text
2.	Removing the cardinality from dates (i.e remove ‘st’, ‘nd’, ‘rd’, ‘th’ from 1st, 2nd, 3rd, xth )
3.	Predicting dates using spacy ‘English-en_core_web_sm model’. (In the future this will be replaced with a custom model)
4.	Standardised the extracted dates using Python build in capabilities into dd/mm/yyyy format 
5.	Issue warning if the input text contains numbers, but no date has been extracted
6.	Generate a structure json output as shown below

```
# Example output

{
  "dates": ["31/06/2019","01/07/2022"],              
  "message": "Success"             
}
```

```
{
  "dates": [],              
  "message": "Warning, dates not extracted correctly"             
}

```

## Ticket-1  Package data science code to be consumed by API development team 

The objective is to productionliase the data science code. The output you produce in this exercise, should be able to be consumed by the data engineering team that is developing the APIs that will expose the ML model. The ask is not to create the API itself. But rather to productionalise the data science code. 
 
The accuracy of the results in terms of exctracting the correct dates and formats is not important for the purpose of this exercise.  The exercise asseses the overall solution design, code structure, coding standards, maintainability, modularity, testing etc 

During work on the solution, please use all the good practices that would be normally used during the development of a production-ready solution.  
Please feel free to use any libraries, patterns or solution structure (including adding projects) that feels right for you.  

During the interview session, the produced solution will be demoed, reviewed and discussed.  
