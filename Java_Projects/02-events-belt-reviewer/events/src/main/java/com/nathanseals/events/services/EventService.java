package com.nathanseals.events.services;



import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.nathanseals.events.models.Event;
import com.nathanseals.events.models.Message;
import com.nathanseals.events.models.User;
import com.nathanseals.events.repositores.EventRepository;
import com.nathanseals.events.repositores.MessageRepository;

@Service
public class EventService {
	@Autowired
	private EventRepository eRepo;
	@Autowired
	private MessageRepository mRepo;
	
	public Event findById(Long id) {
		return this.eRepo.findById(id).orElse(null);
	}
	public Event create(Event event) {
		return this.eRepo.save(event);
	}
	public Event update(Event event) {
		return this.eRepo.save(event);
	}
	public void comment(User user, Event event, String comment) {
		this.mRepo.save(new Message(user, event, comment));
	}
	public void delete(Long id) {
		this.eRepo.deleteById(id);
	}
	public void manageAttendees(Event event, User user, boolean isJoining) {
		if(isJoining) {
			event.getAttendees().add(user);
		} else {
			event.getAttendees().remove(user);
		}
		this.eRepo.save(event);
	}
	public List<Event> findAll() {
		return eRepo.findAll();
	}
}
