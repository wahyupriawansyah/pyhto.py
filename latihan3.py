class BilanganBulat(object):
   def __init__(self, nilai):
      if not isinstance(nilai, int):
         raise TypeError("Nilai harus bertipe bilangan bulat")
      self.nilai = nilai

   
   def __mul__(self, objek):
      if isinstance(objek, int):
         return self.nilai * objek
      elif isinstance(objek, float):
         return float(self.nilai * objek)
      elif isinstance(objek, BilanganBulat):
         return self.nilai * objek.nilai
      else:
         raise TypeError("Objek harus bertipe numerik")
    
	
   def __gt__(self, objek):
      if isinstance(objek, int):
         return self.nilai > objek
      elif isinstance(objek, float):
         return float(self.nilai) > objek
      elif isinstance(objek, BilanganBulat):
         return self.nilai > objek.nilai
      else:
         raise TypeError("Objek harus bertipe numerik")


def main():
   a = BilanganBulat(12)
   b = BilanganBulat(5)
   c = 17
   d = 2.5

   print("DATA:")
   print("a = 12 \nb = 5" "\nc =", c, "\nd =", d)
   print("\nmenampilkan hasil dari operator mul(perkalian)")
   print("a * b: ", a * b)
   print("b * b: ", b * b)
   print("b * d: ", b * d)

   
   print("\nmenampilkan hasil dari operator gt(lebih besar)")
   print("a lebih besar b: ", a > b)
   print("a lebih besar c: ", a > c)
   print("b lebih besar d: ", b > d)
   
   
   
if __name__ == "__main__":
   main()
