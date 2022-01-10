package com.nathanseals.dojosandninjas.services;

import java.util.List;
import org.springframework.stereotype.Service;

import com.nathanseals.dojosandninjas.models.Dojo;
import com.nathanseals.dojosandninjas.models.Ninja;
import com.nathanseals.dojosandninjas.repositories.DojoRepository;
import com.nathanseals.dojosandninjas.repositories.NinjaRepository;
@Service
public class MainService {
	private final DojoRepository dojoRepo;
	private final NinjaRepository ninjaRepo;
	public MainService(DojoRepository dojoRepo, NinjaRepository ninjaRepo) {
		this.dojoRepo = dojoRepo;
		this.ninjaRepo = ninjaRepo;
	}
	//Queries
	public List<Dojo> allDojos() {
		return dojoRepo.findAll();
	}
	public List<Ninja> allNinjas() {
		return ninjaRepo.findAll();
	}
	public Dojo findDojo(Long id) {
		return dojoRepo.findById(id).orElse(null);
	}
	public List<Ninja> ninjasByDojo(String search) {
		return ninjaRepo.findByDojo(search);
	}
	
	//Create
	public Dojo createDojo(Dojo dojo) {
		return dojoRepo.save(dojo);
	}
	public Ninja createNinja(Ninja ninja) {
		return ninjaRepo.save(ninja);
	}
//	public void deleteAll() {
//		dojoRepo.deleteAll();
//	}
}
