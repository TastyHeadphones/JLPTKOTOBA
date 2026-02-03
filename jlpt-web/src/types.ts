export interface VocabularyItem {
    id: string;
    word: string;
    reading: string;
    meaning_cn: string;
    meaning_en: string;
    level: string;
    example_sentence?: string;
    example_reading?: string;
    example_meaning_cn?: string;
    example_meaning_en?: string;
}
