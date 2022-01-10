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
	<h1>Create a new idea:</h1>
	<form:form action="/ideas/create" method="post" modelAttribute="idea">
		<form:hidden value="${ user.id }" path="creator"/>
			<div class="form-group">
				<form:label path="content">What's your idea?</form:label>
				<form:errors path="content"></form:errors>
				<form:input class="form-control" path="content"></form:input>
			</div>
		    <input type="submit" class="btn btn-primary" value="Create Idea">
	</form:form>
	</div>
</body>
</html>