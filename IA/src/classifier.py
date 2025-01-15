def get_scores(text):
    # Mots-clés pour SISR (Systèmes et Réseaux)
    sisr_keywords = [
        'serveur', 'réseau', 'virtualisation', 'sécurité', 'cloud', 'firewall', 'routeur', 'switch', 'dns',
        'maintenance', 'système', 'linux', 'windows server', 'infrastructure', 'vpn', 'backup', 'stockage',
        'datacenter', 'virtual machine', 'active directory', 'supervision', 'monitoring', 'déploiement', 'configuration',
        'administration système', 'cybersécurité', 'pare-feu', 'protocole', 'tcp/ip', 'ftp', 'ssh', 'smtp', 'udp',
        'hyperviseur', 'containers', 'docker', 'kubernetes', 'ip', 'wifi', 'internet des objets', 'networks',
        'cloud computing', 'cisco', 'microsoft', 'routing', 'switching', 'backup', 'ldap', 'vlan', 'nas', 'san',
        'exploitation', 'infrastructure IT', 'automatisation', 'administration réseaux', 'raspberry pi', 'informatique embarquée',
        'monitoring réseau', 'administration cloud', 'docker', 'apache', 'nginx', 'serveur web', 'redhat', 'centos'
    ]

    # Mots-clés pour SLAM (Solutions Logicielles et Applications Métiers)
    slam_keywords = [
        'application', 'base de données', 'développement', 'web', 'html', 'css', 'javascript', 'python', 'java', 'php',
        'sql', 'mysql', 'postgresql', 'oracle', 'mongodb', 'api', 'frontend', 'backend', 'framework', 'node.js', 'angular',
        'react', 'vue.js', 'django', 'flask', 'spring', 'laravel', 'express', 'programmation', 'algorithme', 'modélisation',
        'uml', 'rest', 'soap', 'mobile', 'android', 'ios', 'swift', 'kotlin', 'interface utilisateur', 'design',
        'responsive', 'test unitaire', 'debugging', 'optimisation', 'devops', 'intégration continue', 'gestion de projet',
        'logiciel', 'architecture logicielle', 'git', 'github', 'gestionnaire de version', 'cloud computing', 'microservices',
        'react native', 'xcode', 'android studio', 'typescript', 'webpack', 'mongodb', 'postgres', 'api rest', 'graphql',
        'ui/ux', 'testing', 'mockups', 'cypress', 'selenium', 'jenkins', 'docker', 'redux', 'material ui', 'expressjs',
        'angularjs', 'vuejs', 'typescript', 'docker', 'laravel', 'spring boot', 'nosql', 'firebase', 'angular 2+', 'scrum',
        'oop', 'mvc', 'webapi', 'flutter', 'ionic', 'tdd', 'bachelor informatique', 'frontend developer', 'backend developer'
    ]

    # Liste des mots-clés négatifs spécifiques
    negative_keywords_sisr = ['réseau', 'serveur', 'virtualisation', 'infrastructure', 'vpn', 'cloud', 'firewall', 'tcp/ip']
    negative_keywords_slam = ['html', 'css', 'java', 'mobile', 'développement', 'api', 'frontend', 'backend']

    # Fonction qui vérifie si une phrase négative affecte un mot-clé spécifique
    def apply_negative_logic(text, keywords, negative_keywords, category):
        # Si une des phrases négatives est trouvée dans le texte
        if "je n'aime pas" in text.lower() or "pas de" in text.lower():
            for keyword in keywords:
                # Appliquer la négation uniquement aux mots-clés dans la catégorie pertinente
                if keyword in text.lower():
                    if category == 'SISR' and any(neg_kw in text.lower() for neg_kw in negative_keywords_sisr):
                        print(f"Négatif trouvé pour {keyword} dans la catégorie SISR")
                        return -1  # Retirer un point pour les mots-clés SISR si mentionné après une négation
                    if category == 'SLAM' and any(neg_kw in text.lower() for neg_kw in negative_keywords_slam):
                        print(f"Négatif trouvé pour {keyword} dans la catégorie SLAM")
                        return -1  # Retirer un point pour les mots-clés SLAM si mentionné après une négation
        return 0

    # Calcul des scores SISR et SLAM
    sisr_score = sum(1 for word in sisr_keywords if word in text.lower())
    slam_score = sum(1 for word in slam_keywords if word in text.lower())

    # Appliquer la logique négative uniquement sur les mots-clés pertinents
    sisr_score += apply_negative_logic(text, sisr_keywords, negative_keywords_sisr, 'SISR')
    slam_score += apply_negative_logic(text, slam_keywords, negative_keywords_slam, 'SLAM')

    return sisr_score, slam_score

def classify_text(text):
    sisr_score, slam_score = get_scores(text)
    print(f"Score SISR: {sisr_score}, Score SLAM: {slam_score}")
    if sisr_score > slam_score:
        return "SISR"
    elif slam_score > sisr_score:
        return "SLAM"
    else:
        return "Les deux filières sont possibles"