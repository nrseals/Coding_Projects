package com.nathanseals.greatideas.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.nathanseals.greatideas.models.Idea;
import com.nathanseals.greatideas.repositories.IdeaRepository;

@Service
public class IdeaService {
	@Autowired
	private IdeaRepository ideaRepository;
	
	public List<Idea> findAllIdeas(){
		return this.ideaRepository.findAll();
	}
	
	public Idea createOneIdea(Idea idea) {
		return this.ideaRepository.save(idea);
	}
	
	public Idea findOneIdea(Long id) {
		return this.ideaRepository.findById(id).orElse(null);
	}
	
	public Idea updateOneIdea(Idea idea) {
		return this.ideaRepository.save(idea);
	}
	
	public void deleteOneIdea(Long id) {
		this.ideaRepository.deleteById(id);
	}
}
