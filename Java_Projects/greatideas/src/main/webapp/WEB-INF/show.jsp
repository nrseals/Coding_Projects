<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<!DOCTYPE html>
<html>
	<head>
		<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" 
			rel="stylesheet"/>
		<meta charset="UTF-8">
<title>Great Ideas</title>
</head>
<body>
	<div class="container">
		<nav class="navbar navbar-expand-lg navbar-light bg-light">
			<div class="container-fluid">
	  			<a class="navbar-brand" href="/ideas">Great Ideas</a>
	  			<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
	    			<span class="navbar-toggler-icon"></span>
	  			</button>
	  			<div class="collapse navbar-collapse" id="navbarNav">
	    		<ul class="navbar-nav">
	      			<li class="nav-item">
	        			<a class="nav-link" aria-current="page" href="/ideas/new">New Idea</a>
	      			</li>
	      			<li class="nav-item">
	        			<a class="nav-link" href="/logout">Logout</a>
	        		</li>
	        	</ul>
	        	</div>
	        </div>
	     </nav>
	     <div class="container">
	     	<h1>${ idea.content }</h1>
	     	<h3>Created By: ${ idea.creator.name }</h3>
	     	<a class="btn btn-lg btn-outline-warning" href="/ideas/${ idea.id }/edit">Edit Idea</a>
	     </div>
	 </div>
</body>
</html>