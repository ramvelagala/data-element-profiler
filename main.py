vectorizer = CountVectorizer(max_features=70000,
                                 analyzer="word",
                                 lowercase=False,
                                 tokenizer=lambda doc: doc,
                                 ngram_range=(1, 1),
                                 vocabulary=nlp_terms,
                                 min_df=0.0)
    column_names = vectorizer.vocabulary


A_train = vectorizer.fit_transform(X_train['mbr_ngrams'])

    # In[13]:

    # transform the in-time test and out-of-time dataset that will be used to compare performance of champion vs challenger
    A_test = vectorizer.transform(X_test['mbr_ngrams'])
    A_oot = vectorizer.transform(df_oot['mbr_ngrams'])

    # convert sparse matrix to dense matrix
    X_train_transformed = pd.DataFrame(A_train.todense(),
                                       columns=vectorizer.get_feature_names_out())
    X_test_transformed = pd.DataFrame(A_test.todense(),
                                      columns=vectorizer.get_feature_names_out())
    oot_transformed = pd.DataFrame(A_oot.todense(),
                                   columns=vectorizer.get_feature_names_out())
    # create out-of-time series of labels
    y_oot = df_oot['answer']
model_path = config['DEFAULT']['champion_model_path']
    print(model_path)
    # load champion pickle
    with open(model_path, 'rb') as fmodel:
        champion_model = pickle.load(fmodel)
    # create challenger model copy
    challenger_model = pickle.loads(pickle.dumps(champion_model))
tratified_kfold = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

    # create randomized cross validation search
    # we can go with either n_iter==300 or n_iter==500 depending on workspace resources
    random_search = RandomizedSearchCV(challenger_model, param_distributions=params,
                                       n_iter=10, scoring='balanced_accuracy',
                                       cv=stratified_kfold, n_jobs=-1, verbose=1)

    # execute randomized 5-fold stratified cross validation with 500 iterations which will result in 2,500 different parameter combinations
    random_search.fit(X_train_transformed, y_train)
