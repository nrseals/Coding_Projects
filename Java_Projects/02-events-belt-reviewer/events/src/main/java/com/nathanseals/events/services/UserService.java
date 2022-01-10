package com.nathanseals.events.services;

import org.mindrot.jbcrypt.BCrypt;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.nathanseals.events.models.User;
import com.nathanseals.events.repositores.UserRepository;

@Service
public class UserService {
	@Autowired
	private UserRepository uRepo;
	//Find By Id
	public User findById(Long id) {
		return this.uRepo.findById(id).orElse(null);
	}
	//Create User
	public User registerUser(User user) {
		String hashed = BCrypt.hashpw(user.getPassword(), BCrypt.gensalt());
		user.setPassword(hashed);
		return this.uRepo.save(user);
	}
	//Find by Email
	public User getUserByEmail(String email) {
		return this.uRepo.findByEmail(email);
	}
	//Authenticate
	public boolean authenticateUser(String email, String password) {
		User user = this.uRepo.findByEmail(email);
		if(user == null)
			return false;
		
		return BCrypt.checkpw(password, user.getPassword());
	}
}
