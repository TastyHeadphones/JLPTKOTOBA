export interface VocabularyItem {
    id: string;
    word: string;
    reading?: string; // Optional old format
    kanji_reading?: string; // New format for Furigana
    meaning_cn: string;
    meaning_en: string;
    level: string;
    example_sentence?: string;
    example_reading?: string;
    example_meaning_cn?: string;
    example_meaning_en?: string;
}
