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
	<title>Events: Belt Review!</title>
</head>
	<body>
		<div class="container">
			<h2>Welcome, ${ user.firstName }</h2>
			<div class="float float-left">
				<h3>Here are some events:</h3>
				<table class="table table-hover">
					<thead>
						<tr>
							<th>Name</th>
							<th>Date</th>
							<th>City</th>
							<th>Host</th>
							<th>Action/Status</th>
						</tr>
					</thead>
					<tbody>
					<c:forEach items="${ events }" var="event">
						<tr>
							<td><a href="/events/${ event.id }">${ event.name }</a></td>
							<td>${ event.date }</td>
							<td>${ event.city }</td>
							<td>${ event.planner.firstName }</td>
							<td>
							<c:choose>
								<c:when test="${ event.planner.id == user.id }">
									<div class="container" id="edit-delete">
										<a class="btn btn-sm btn-warning" href="/events/${ event.id }/edit">Edit</a> |
										<form class="delete-form" action="/events/${ event.id }" method="post">
											<input type="hidden" name="_method" value="delete" />
											<button class="btn btn-sm btn-danger">Delete</button>
										</form>
									</div>
								</c:when>
								<c:otherwise>
									<c:choose>
										<c:when test="${ event.attendees.contains(user) }">
											<span>Joining <a class="btn btn-sm btn-outline-primary" href="/events/${ event.id }/a/cancel">Cancel</a></span>
										</c:when>
										<c:otherwise>
											<a class="btn btn-sm btn-primary" href="/events/${ event.id }/a/join">Join</a>								
										</c:otherwise>
									
									</c:choose>
								</c:otherwise>
							</c:choose>
							</td>
						</tr>
					</c:forEach>
					</tbody>
				</table>
			</div>
		</div>
	</body>
</html>