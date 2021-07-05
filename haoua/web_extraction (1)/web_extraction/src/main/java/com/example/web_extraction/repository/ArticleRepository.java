package com.example.web_extraction.repository;

import com.example.web_extraction.model.Article;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.List;
@Repository

public interface ArticleRepository extends MongoRepository<Article, ArrayList<String>> {
}
